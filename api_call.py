import requests
import pandas as pd


def get_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 37.54,
        "longitude": -77.44,
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

    return pd.DataFrame(data["hourly"])