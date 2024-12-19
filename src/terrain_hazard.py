import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from scipy.ndimage import zoom
import rasterio
import threading

def load_dem(file_path):
    """Load the DEM (Digital Elevation Model) data."""
    with rasterio.open(file_path) as src:
        dem_data = src.read(1)
    return dem_data

def downsample_dem(dem_data, scale_factor=0.1):
    """Downsample the DEM data by the given scale factor."""
    return zoom(dem_data, scale_factor, order=3)

def plot_2d_elevation(dem_data):
    """Plot the 2D elevation map using Matplotlib."""
    plt.figure(figsize=(8, 6))
    plt.imshow(dem_data, cmap='terrain', origin='upper')
    plt.colorbar(label='Elevation (meters)')
    plt.title('2D Elevation Map')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    

    plt.show()

def plot_3d_elevation_plotly(dem_data):
    """Plot the 3D elevation map using Plotly for better performance."""
    # meshgrid for plotting
    x = np.arange(dem_data.shape[1])
    y = np.arange(dem_data.shape[0])
    x, y = np.meshgrid(x, y)

    #3D surface plot Plotly
    fig = go.Figure(data=[go.Surface(z=dem_data, x=x, y=y, colorscale='Viridis')])  # Use a valid color scale

    fig.update_layout(
        title="3D Terrain Map",
        scene=dict(
            xaxis_title='Longitude',
            yaxis_title='Latitude',
            zaxis_title='Elevation (meters)'
        ),
        autosize=True
    )

    #3D plot in the browser
    fig.show()

def plot_3d_elevation_matplotlib(dem_data):
    """Plot the 3D surface of the DEM data using Matplotlib."""
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # meshgrid for plotting
    x = np.arange(dem_data.shape[1])
    y = np.arange(dem_data.shape[0])
    x, y = np.meshgrid(x, y)

    ax.plot_surface(x, y, dem_data, cmap='viridis', edgecolor='k', rstride=20, cstride=20, alpha=0.6)

    #labels
    ax.set_title('3D Terrain (Elevation) Map')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Elevation (meters)')

    # Show the plot
    plt.show()

def main():
    """Main function to load the DEM and plot the 2D and 3D elevation maps."""
    # Load DEM data
    dem_data = load_dem('D:/Hazard_Map/data/earth.tif')

    # Downsample
    dem_data_resampled = downsample_dem(dem_data, scale_factor=0.05)

    thread_2d = threading.Thread(target=plot_2d_elevation, args=(dem_data,))
    thread_2d.start()


    plot_3d_elevation_plotly(dem_data_resampled)

    thread_2d.join()

if __name__ == "__main__":
    main()
