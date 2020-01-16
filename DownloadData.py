from __future__ import absolute_import, division, print_function, unicode_literals
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import geopandas as gpd
import folium
from shapely.geometry import MultiPolygon, Polygon
from datetime import date
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display
from PIL import Image
import os
import pathlib
import rasterio
from rasterio import plot
from pyrsgis import raster 

user='russelljbrown'
password='16Characterslong'
# connect to the API
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
# search by polygon, time, and Hub query keywords
footprint = geojson_to_wkt(read_geojson('/home/russell/XCity/gsonData/test.geojson'))
products = api.query(footprint,
                     date = ('20190225', '20190227'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0, 20))
# download all results from the search
api.download_all(products)
# GeoJSON FeatureCollection containing footprints and metadata of the scenes
api.to_geojson(products)
# GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries
api.to_geodataframe(products)
print("finished")
