# Terrain Hazard Mapping Project

This project is designed to process and visualize Digital Elevation Model (DEM) data, creating both **2D and 3D terrain hazard maps**. The visualizations are produced using **Matplotlib** for 2D plots and **Plotly** for interactive 3D plots. The project also includes downsampling of DEM data for better performance.

## Requirements

### Python Version:
- **Python 3.7 or higher**

### Libraries/Dependencies:

You can install all the necessary libraries using `pip`. The required libraries for this project are:

- `numpy` (for numerical operations)
- `matplotlib` (for creating static 2D plots)
- `plotly` (for creating interactive 3D plots)
- `scipy` (for downsampling the DEM data)
- `rasterio` (for reading DEM data from GeoTIFF files)
- `threading` (for running the 2D and 3D plots simultaneously)

You can install these libraries using the following command:

```bash
pip install numpy matplotlib plotly scipy rasterio

Alternatively, you can install all the requirements at once by running:

bash
Copy code
pip install -r requirements.txt
Where requirements.txt contains the following:

Copy code
numpy
matplotlib
plotly
scipy
rasterio
Optional (for 3D plotting with Plotly):
If you're using Plotly for the first time, it may ask you to install additional dependencies for rendering the plots in a browser. Ensure you have an internet connection as Plotly may need access to its cloud service.

System Requirements:
Operating System: Windows, macOS, or Linux
RAM: 8 GB (recommended 16 GB for better performance)
Disk Space: The DEM file size could be large, so ensure enough disk space is available (e.g., 100 MB or more for a single DEM).
Setup and Installation
Clone the repository (if applicable):

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Download DEM Data:

You can obtain the DEM file from any relevant source (e.g., SRTM, USGS, or other sources of DEM data).
Make sure the DEM file is in the GeoTIFF format (e.g., terrain_data.tif).
File Structure:

bash
Copy code
project_directory/
├── data/
│   └── terrain_data.tif        # Your DEM file
├── src/
│   └── terrain_hazard.py      # Main script for visualization
├── requirements.txt           # List of required Python libraries
└── README.md                  # Project documentation
Usage
Running the Script:
To run the script and generate both 2D and 3D terrain hazard maps, execute the following command in your terminal or command prompt:

bash
Copy code
python src/terrain_hazard.py
This will:

Load the DEM data from the specified file path.
Downsample the DEM data for better performance in 3D plotting.
Plot a 2D elevation map using Matplotlib (in a separate window).
Plot a 3D terrain map using Plotly (in your default web browser).
Sample Execution:
bash
Copy code
python src/terrain_hazard.py
After running the command, you will see:
2D Elevation Map using Matplotlib — This will open in a static window.
3D Terrain Map using Plotly — This will open in your default web browser and is interactive.
Both windows will be open simultaneously.

Optional 3D Plotting with Matplotlib:
You can replace the Plotly 3D plot with Matplotlib by commenting/uncommenting the respective function calls in the script.

To use Matplotlib for 3D plotting:

In the main() function, comment out the line:
python
Copy code
plot_3d_elevation_plotly(dem_data_resampled)
Uncomment the line:
python
Copy code
plot_3d_elevation_matplotlib(dem_data_resampled)
This will generate the 3D plot using Matplotlib, which will open in a separate window.

How It Works
2D Plot:
The 2D elevation map is displayed using Matplotlib's imshow() function, which renders the DEM data with a color map to represent elevation levels.
The 2D plot will remain open until the user manually closes it.
3D Plot:
The 3D terrain map is created using Plotly, which produces an interactive plot rendered in a web browser.
This plot allows for zooming, rotating, and panning.
Downsampling:
The DEM data is downsampled using SciPy's zoom() function to reduce the resolution, improving performance for 3D plotting. The downsampling factor can be adjusted (default is 0.05).
Threading for Simultaneous Plotting:
The 2D plot is displayed in a separate thread, so it does not block the 3D plot from being displayed in the browser.
This allows both plots to be visible simultaneously.
Troubleshooting
2D plot closes quickly:

Ensure that the plt.show() method is not being prematurely closed. The code is set to keep the plot open until manually closed.
3D Plot doesn't open:

Ensure your internet connection is active, as Plotly might need it to render the plot in the browser.
If you prefer to use Matplotlib for 3D plotting, make sure you have the necessary dependencies installed.
Performance Issues:

If the 3D plot is slow, try reducing the resolution of the DEM data or downsample it more aggressively. This will improve performance at the cost of less detail in the 3D plot.
No Display on Matplotlib:

If the 2D plot window doesn't appear or closes too quickly, ensure that you are not running the script inside an IDE that might close the window immediately after execution. Try running it from the command line instead.
