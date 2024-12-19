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
pip install numpy matplotlib plotly rasterio scipy
