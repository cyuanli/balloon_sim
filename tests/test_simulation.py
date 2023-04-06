# tests/test_simulation.py

import pytest
from unittest.mock import Mock, patch
from simulation import Balloon, Trajectory
from weather_api import BaseWeatherAPI, OpenWeatherMapAPI


class MockWeatherAPI(BaseWeatherAPI):
    def fetch_wind_data(self, locations):
        pass

    def fetch_wind_data_at_time(self, locations, time):
        pass


def test_balloon_initialization():
    balloon = Balloon(40.7128, -74.0060, 1000.0)
    assert balloon.lat == 40.7128
    assert balloon.lon == -74.0060
    assert balloon.altitude == 1000.0


@pytest.fixture
def mock_weather_api():
    with patch.object(MockWeatherAPI, "fetch_wind_data") as mock_fetch_wind_data:
        mock_fetch_wind_data.return_value = [(1.0, 1.0)]
        yield MockWeatherAPI("dummy_key")


def test_trajectory_initialization(mock_weather_api):
    balloon = Balloon(40.7128, -74.0060, 1000.0)
    trajectory = Trajectory(mock_weather_api, balloon)

    assert trajectory.api == mock_weather_api
    assert trajectory.balloon == balloon
    assert trajectory.path == [(40.7128, -74.0060)]


def test_trajectory_simulation(mock_weather_api):
    balloon = Balloon(40.7128, -74.0060, 1000.0)
    trajectory = Trajectory(mock_weather_api, balloon)

    path = trajectory.simulate(duration=3, time_step=1.0)

    assert len(path) == 4
    assert path == [
        (40.7128, -74.0060),
        (41.7128, -73.0060),
        (42.7128, -72.0060),
        (43.7128, -71.0060),
    ]
