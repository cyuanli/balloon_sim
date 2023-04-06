import os
import argparse
from dotenv import load_dotenv
from weather_api import OpenWeatherMapAPI
from simulation import Balloon, Trajectory
from animation import BalloonTrajectoryAnimation


def main():
    # Load environment variables from the .env file
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Simulate the trajectory of a weather balloon and generate an animation."
    )
    parser.add_argument("--lat", type=float, required=True, help="Initial latitude of the balloon.")
    parser.add_argument(
        "--lon", type=float, required=True, help="Initial longitude of the balloon."
    )
    parser.add_argument(
        "--altitude",
        type=float,
        default=1000.0,
        help="Initial altitude of the balloon (default: 1000.0 meters).",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=24.0,
        help="Duration of the simulation in hours (default: 6.0 hours).",
    )
    parser.add_argument(
        "--time_step",
        type=float,
        default=0.5,
        help="Time step between simulation points in hours (default: 0.5 hours).",
    )
    parser.add_argument(
        "--output",
        default="trajectory_animation.png",
        help="Output file name for the animation (default: trajectory_animation.png).",
    )

    args = parser.parse_args()

    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ValueError(
            "The environment variable 'OPENWEATHERMAP_API_KEY' is not set. "
            "Please set it to your OpenWeatherMap API key."
        )

    api = OpenWeatherMapAPI(api_key)
    balloon = Balloon(args.lat, args.lon, args.altitude)
    trajectory = Trajectory(api, balloon)
    path = trajectory.simulate(duration=args.duration, time_step=args.time_step)

    animation = BalloonTrajectoryAnimation(path)
    animation.animate(output_file=args.output)

    print(f"Trajectory animation saved to {args.output}")


if __name__ == "__main__":
    main()
