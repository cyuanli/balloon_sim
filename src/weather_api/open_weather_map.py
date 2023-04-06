import math
from typing import List, Tuple
import requests
from .base_api import BaseWeatherAPI


class OpenWeatherMapAPI(BaseWeatherAPI):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _parse_wind_data(self, data):
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"]

        # Convert wind speed and direction to u_wind and v_wind components
        u_wind = wind_speed * math.cos(math.radians(wind_direction))
        v_wind = wind_speed * math.sin(math.radians(wind_direction))

        return u_wind, v_wind

    def fetch_wind_data(self, coordinates: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        wind_data = []

        for lat, lon in coordinates:
            response = requests.get(
                self.base_url,
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": self.api_key,
                    "units": "metric",
                },
                timeout=10,
            )

            response_data = response.json()
            self._parse_wind_data(response_data)
            wind_data.append(self._parse_wind_data(response_data))

        return wind_data

    def fetch_wind_data_at_time(
        self, coordinates: List[Tuple[float, float]], time: str
    ) -> List[Tuple[float, float]]:
        raise NotImplementedError(
            "OpenWeatherMap API does not support fetching historical wind data."
        )
