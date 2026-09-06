import json
from datetime import datetime, timezone
from pathlib import Path
import requests

url = "https://opensky-network.org/api/states/all"
response = requests.get(url)
data = response.json()

flights = data.get("states", [])

clean_flights = []

for flight in flights:
    clean_flights.append(
        {
            "icao24": flight[0],
            "callsign": flight[1].strip() if flight[1] else None,
            "longitude": flight[5],
            "latitude": flight[6],
            "velocity": flight[9],
            "vertical_rate": flight[11],
            "geo_altitude": flight[13],
        }
    )

now = datetime.now(timezone.utc)
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

folder_path = Path(f"data/s3/aviation-bronze/year={year}/month={month}/day={day}")
folder_path.mkdir(parents=True, exist_ok=True)

file_path = folder_path / f"telemetry_{now.strftime('%H%M%S')}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(clean_flights, f, ensure_ascii=False)

print(f"Saved {len(clean_flights)} records to: {file_path}")