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
