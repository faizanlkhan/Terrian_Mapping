import rasterio
import numpy as np
import matplotlib.pyplot as plt

def load_dem(file_path):
    with rasterio.open(file_path) as src:
        dem_data = src.read(1)
    return dem_data

def plot_dem(dem_data):
    plt.imshow(dem_data, cmap='terrain')
    plt.colorbar(label="Elevation (meters)")
    plt.title("DEM - Terrain Elevation")
    plt.show()

def calculate_slope(dem_data):
    grad_x = np.gradient(dem_data, axis=0)
    grad_y = np.gradient(dem_data, axis=1)
    slope = np.sqrt(grad_x**2 + grad_y**2)
    return slope

def plot_slope(slope_data):
    plt.imshow(slope_data, cmap='coolwarm')
    plt.colorbar(label="Slope (degrees)")
    plt.title("Slope Map")
    plt.show()

if __name__ == "__main__":
    dem_data = load_dem('D:/Hazard_Map/data/ch2moon.tif')
    plot_dem(dem_data)
    slope_data = calculate_slope(dem_data)
    plot_slope(slope_data)