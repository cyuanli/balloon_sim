import math
from typing import List, Tuple
from weather_api import BaseWeatherAPI
from .balloon import Balloon


class Trajectory:
    def __init__(self, api: BaseWeatherAPI, balloon: Balloon):
        self.api = api
        self.balloon = balloon
        self.path = [(balloon.lat, balloon.lon)]

    def _update_location(self, wind_components, time_step):
        u_wind, v_wind = wind_components

        # Calculate the change in latitude and longitude
        dlat = (
            v_wind * time_step * 3600 / 111_139
        )  # Convert hours to seconds, and meters to degrees
        dlon = (
            u_wind * time_step * 3600 / (111_139 * math.cos(math.radians(self.balloon.lat)))
        )  # Convert hours to seconds, and meters to degrees

        # Update the balloon's location
        self.balloon.lat += dlat
        self.balloon.lon += dlon

    def simulate(self, duration: float, time_step: float = 1.0) -> List[Tuple[float, float]]:
        total_time = 0

        while total_time < duration:
            wind_data = self.api.fetch_wind_data([self.path[-1]])

            # Update balloon position based on wind data
            self._update_location(wind_data[0], time_step)

            # Add updated position to the path
            self.path.append((self.balloon.lat, self.balloon.lon))

            total_time += time_step

        return self.path
