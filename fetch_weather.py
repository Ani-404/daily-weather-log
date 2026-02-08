import requests
from datetime import datetime

URL = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"

data = requests.get(URL).json()

temp = data["current_weather"]["temperature"]
today = datetime.utcnow().strftime("%Y-%m-%d")

with open("weather.csv", "a") as f:
    f.write(f"{today},{temp}\n")

print("Logged:", today, temp)