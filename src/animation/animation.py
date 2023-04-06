import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


class BalloonTrajectoryAnimation:
    def __init__(self, trajectory):
        self.trajectory = trajectory

    def animate(self, output_file: str = "trajectory_animation.mp4"):
        # Create a new figure and add a map with coastlines and borders
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)

        # Plot the balloon's trajectory on the map
        lats, lons = zip(*self.trajectory)
        ax.plot(lons, lats, "r", transform=ccrs.PlateCarree())

        # Set the map's extent based on the trajectory
        min_lat, max_lat = min(lats), max(lats)
        min_lon, max_lon = min(lons), max(lons)
        ax.set_extent([min_lon - 5, max_lon + 5, min_lat - 5, max_lat + 5], crs=ccrs.PlateCarree())

        # Save the animation to a file
        plt.savefig(output_file)
