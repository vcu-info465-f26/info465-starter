import requests
import pandas as pd

# Richmond, Virginia coordinates
latitude = 37.54
longitude = -77.44

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "wind_speed_10m"
    ],
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
    "timezone": "America/New_York"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

weather = pd.DataFrame(data["hourly"])

print(weather.head(20))