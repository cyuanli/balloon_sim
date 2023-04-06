import os
import pytest
from animation import BalloonTrajectoryAnimation


def test_animation_file_creation(tmp_path):
    trajectory = [
        (40.7128, -74.0060),
        (41.7128, -73.0060),
        (42.7128, -72.0060),
        (43.7128, -71.0060),
    ]
    animation = BalloonTrajectoryAnimation(trajectory)

    output_file = tmp_path / "test_output.png"
    animation.animate(output_file=output_file)

    assert output_file.is_file()
