import requests
import csv
import os
from datetime import datetime, timezone

URL = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.21&current_weather=true"

data = requests.get(URL).json()

weather = data["current_weather"]

temp = weather["temperature"]
wind = weather["windspeed"]
time = weather["time"]

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

file_exists = os.path.isfile("weather.csv")

with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["date", "api_time", "temperature_C", "windspeed_kmh"])

    writer.writerow([today, time, temp, wind])

print("Logged:", today, temp)