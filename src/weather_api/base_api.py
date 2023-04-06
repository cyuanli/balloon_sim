from abc import ABC, abstractmethod
from typing import List, Tuple


class BaseWeatherAPI(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def fetch_wind_data(self, coordinates: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """
        Fetch wind speed data from the API for a given list of coordinates.

        :param coordinates: List of tuples containing latitude and longitude pairs.
        :return: List of tuples containing wind speed data (u_wind, v_wind) corresponding to the
            input coordinates.
        """
        pass

    @abstractmethod
    def fetch_wind_data_at_time(
        self, coordinates: List[Tuple[float, float]], time: str
    ) -> List[Tuple[float, float]]:
        """
        Fetch wind speed data from the API for a given list of coordinates at a specific time.

        :param coordinates: List of tuples containing latitude and longitude pairs.
        :param time: A string representing the time for which the wind data should be fetched
            (e.g., "2023-04-07T12:00:00Z").
        :return: List of tuples containing wind speed data (u_wind, v_wind) corresponding to the
            input coordinates.
        """
        pass
