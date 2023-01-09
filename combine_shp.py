import os
import geopandas as gpd

# Set the path to the directory containing the shapefiles
shapefile_dir = '/path/to/shapefiles'

# Initialize an empty list to store the shapefiles
shapefiles = []

# Traverse through the directory and add the shapefiles to the list
for root, dirs, files in os.walk(shapefile_dir):
    for file in files:
        if file.endswith('.shp'):
            shapefiles.append(os.path.join(root, file))

# Combine the shapefiles into a single GeoDataFrame
combined_shapefile = gpd.GeoDataFrame(pd.concat([gpd.read_file(shp) for shp in shapefiles]))

# Save the combined shapefile
combined_shapefile.to_file('/path/to/combined_shapefile.shp', driver='ESRI Shapefile')
