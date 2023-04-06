from unittest.mock import Mock, patch
import pytest
from weather_api import BaseWeatherAPI, OpenWeatherMapAPI


def test_base_weather_api_abstract_class():
    with pytest.raises(TypeError):
        _ = BaseWeatherAPI("dummy_key")


@pytest.fixture
def mock_open_weather_map_api():
    with patch("weather_api.open_weather_map.requests.get") as mock_get:
        mock_get.return_value = Mock(json=lambda: {"wind": {"speed": 5, "deg": 270}})
        api = OpenWeatherMapAPI("dummy_key")
        yield api


def test_open_weather_map_api_fetch_wind_data(mock_open_weather_map_api: OpenWeatherMapAPI):
    coordinates = [(40.7128, -74.0060)]
    wind_data = mock_open_weather_map_api.fetch_wind_data(coordinates)

    assert len(wind_data) == 1
    assert wind_data[0] == (1350, 1350)


def test_open_weather_map_api_fetch_wind_data_at_time(mock_open_weather_map_api: OpenWeatherMapAPI):
    coordinates = [(40.7128, -74.0060)]
    time = "2023-04-07T12:00:00Z"

    with pytest.raises(NotImplementedError):
        _ = mock_open_weather_map_api.fetch_wind_data_at_time(coordinates, time)
