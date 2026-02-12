# Daily Weather Log

A tiny, professional project that fetches current weather once per day and commits the result to the default branch.  
This creates a growing dataset and consistent Git activity while remaining practical and resume-friendly.

**Data source:** Open-Meteo (free public API)  
**Hosted on:** GitHub

---

## What this project does

- Calls a free weather API once per day.
- Appends one row per day to `weather.csv`.
- Uses a GitHub Actions workflow to run the script and push commits using a Personal Access Token (PAT) so commits are attributed to your account and show on your contribution graph.
- Minimal, real-world example demonstrating HTTP APIs, simple ETL, and CI automation.

---

## Repository layout

```
.
├── README.md
├── weather.csv           # created/updated by the workflow
├── fetch_weather.py      # idempotent, retrying Python script
└── .github/
    └── workflows/
        └── daily.yml     # GitHub Actions workflow (schedules daily run)
```

---

## Quickstart — personal items you must set

1. **Create a GitHub Personal Access Token (PAT)**  
   - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic).  
   - Give it a name (e.g., `daily-weather`) and enable the `repo` scope.  
   - Copy the token (starts with `ghp_...`).

2. **Add repository secrets** (Repo → Settings → Secrets and variables → Actions → New repository secret):  
   - `PERSONAL_TOKEN` = `<your PAT>`  
   - `GIT_NAME` = your display name (e.g., `Animesh Kumar`)  
   - `GIT_EMAIL` = your **verified GitHub email** (this must match a verified email on your account for commits to count as your contributions)

3. Optional environment variables (set in the workflow or run locally):  
   - `LATITUDE`, `LONGITUDE` — defaults are Delhi: `28.61`, `77.21`.  
   - `TZ` — timezone label (e.g., `Asia/Kolkata`). If unavailable, the script falls back to UTC.

> **Important:** `GIT_EMAIL` must be a verified email on your GitHub account; otherwise commits will not be counted as your contributions.

---

## Recommended workflow push snippet

Include a safe push step in your workflow similar to this (the example assumes the default branch is `main` — change if yours differs):

```yaml
- name: Commit and push
  env:
    TOKEN: ${{ secrets.PERSONAL_TOKEN }}
  run: |
    git config user.name "${{ secrets.GIT_NAME }}"
    git config user.email "${{ secrets.GIT_EMAIL }}"

    git add weather.csv
    git commit -m "chore: daily weather log" || echo "no changes to commit"

    # Incorporate remote changes before pushing to avoid rejected pushes
    git pull --rebase "https://x-access-token:${TOKEN}@github.com/${{ github.repository }}.git" main || true
    git push "https://x-access-token:${TOKEN}@github.com/${{ github.repository }}.git" main
```

---

## Run locally (test)

1. Install dependencies:
```bash
python -m pip install requests
```

2. Run:
```bash
python fetch_weather.py
```

3. Inspect `weather.csv`. The script avoids duplicate entries for the same date.

---

## Troubleshooting

- **Push rejected: `Updates were rejected because the remote contains work that you do not have locally`**  
  Add the `git pull --rebase ...` step shown above so the Action rebases local commits on latest remote history before pushing.

- **Commits show as `github-actions[bot]`**  
  Ensure the workflow uses your PAT for push (not `GITHUB_TOKEN`) and that `git config user.email` is set to your verified email.

- **Contribution square not showing**  
  - Confirm commit author email is verified on your account.  
  - Commit must be on the repository’s default branch.  
  - Wait a few minutes (sometimes up to 30) for the contribution graph to update.

- **Duplicates for same date**  
  The provided `fetch_weather.py` is idempotent and will skip adding a row for the same date. If duplicates appear, check the Action logs.

---

## Security notes

- Keep the PAT private; store it only as a repository secret.  
- Use the minimum required scope (`repo`). Rotate or revoke the token if compromised.

---

## Extending the project (small ideas)

- Auto-generate a weekly `README.md` summary (mean/min/max) and commit it.  
- Create a weekly `plot.png` (matplotlib) and commit for a visible dashboard.  
- Collect additional metrics such as humidity or pressure if the API provides them.

---



## About the script

`fetch_weather.py` features:
- Retries with exponential backoff on network errors.
- Creates header row if `weather.csv` does not exist.
- Appends a single row per date: `date, time_observed_utc, temperature_c, windspeed_kmh, winddirection_deg`.
- Safe to run manually or in GitHub Actions.

---

## License

Provided as-is for learning and demonstration. Use freely for personal projects and interview demos.

---

## Repo

https://github.com/Ani-404/daily-weather-log
