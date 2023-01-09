# Combine Shapefiles
Combine Multiple Shapefiles into one with Python



Shapefiles are a popular geospatial data format commonly used in geographic information systems (GIS) software. They store both the geometry and attributes of spatial features, such as points, lines, and polygons. If you have multiple shapefiles that you want to merge into a single file, Python can make it easy to do so.

To combine shapefiles using Python, we will need to use the following libraries:

1.  **os**: This library will be used to traverse through the directories and files on your system.
2.  **geopandas**: This library will be used to read and write shapefiles, as well as manipulate the data within them.

Here is the script that demonstrates how to combine multiple shapefiles into a single shapefile:

```python
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
```
First, we set the path to the directory containing the shapefiles that we want to merge. Next, we initialize an empty list called `shapefiles` to store the path of each shapefile that we find. We then use the `os.walk` function to traverse through the directory and its subdirectories, looking for shapefiles (identified by their .shp file extension). Whenever we find a shapefile, we add its path to the `shapefiles` list.

Once we have a list of all the shapefiles in the specified directory, we can use the `concat` function from `pandas` to combine them into a single GeoDataFrame. Finally, we use the `to_file` function from `geopandas` to save the combined shapefile to the specified location on our system.

And that's it! With just a few lines of code, we were able to merge multiple shapefiles into a single file using Python. I hope this post was helpful and that you now feel confident combining shapefiles in Python. Happy coding!
