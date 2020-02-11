from glob import glob
import os
import rasterio
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from osgeo import gdal

imagePath = "/home/russell/XCity/Export"
dict=glob(imagePath + "/*/")
trueColourCount=0
falseColourCount=0
for i in dict:
    tempDict = i+"GRANULE"
    subDict = glob(tempDict+"/*/")
    for j in subDict:
        tempSubDict = j + "IMG_DATA/R10m"
        for file in os.listdir(tempSubDict):
            filePath = tempSubDict+"/"+file
            if "B02_10m.jp2" in file:
                band2 = rasterio.open(filePath, driver='JP2OpenJPEG') #blue
                #series_of_band2=series_of_band2.append(band2)
                torch.tensor(band2)
            if "B03_10m.jp2" in file:
                band3 = rasterio.open(filePath, driver='JP2OpenJPEG') #green
                torch.tensor(band3)
                #series_of_band3 = series_of_band8.append(band3)
            if "B04_10m.jp2" in file:
                band4 = rasterio.open(filePath, driver='JP2OpenJPEG') #red
                print("This Line: ")
                print(band4)
                torch.tensor(band4)
            if "B08_10m.jp2" in file:
                band8 = rasterio.open(filePath, driver='JP2OpenJPEG') #nir
                torch.tensor(band8)
                #series_of_band8 = series_of_band8.append(band8)
print(band2)
print("")
print(band3)
print("")
print(band4)
print("")
print(band8)
print("")
