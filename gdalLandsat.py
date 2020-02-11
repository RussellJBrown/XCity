from osgeo import gdal
import numpy as np
import os
import sys
from PIL import Image
import re
import geopandas as gpd
import folium
import scipy.misc as sm
import math
import cv2
import random
import h5py
from numpy import save

def readLandsatBands(filepath, band2, band3, band4, band5):
    try:
        #Landsat 8
        #if band4 != 0 and band5 != 0:
         #   reshapeImage(filepath,band4,band5)
        #Landsat 4-7 Comparison
        if band3 != 0 and band4!=0:
           reshapeImage(filepath,band3,band4)
        reviewReds(filepath)
        print("Finished NDVI Process")
    except Exception as e:
        print(e)

def reviewReds(filepath):
    #Look into JPEG compression
    print("Starting NDVI Process")
    np.seterr(over='ignore')
    RED = gdal.Open(filepath+"/RED.TIF")
    NIR = gdal.Open(filepath+"/NIR.TIF")
    RED= np.array(RED.GetRasterBand(1).ReadAsArray())
    NIR= np.array(NIR.GetRasterBand(1).ReadAsArray())
    numrows = RED.shape[0]
    numcols = RED.shape[1]
    img = np.zeros((numrows,numcols,3),np.uint8)
    landClassification = np.empty((numrows,numcols),dtype=object)
    for x in range(numrows):
        for y in range(numcols):
            redV=RED[x,y]
            nirV=NIR[x,y]
            if(redV+nirV!=0):
                NDVI = (nirV - redV) / (redV + nirV)
                #.199 produces a bit to many results
                if NDVI>2.5:
                    img[x, y] = [255, 0, 0]
                    landClassification[x, y] = "Water"
                elif NDVI>=0.3 and NDVI<2.5:
                    img[x, y] = [0, 128, 0]
                    landClassification[x, y] = "Heavy Vegetation"
                #elif NDVI>=0.3 and NDVI<0.5:
                 #   img[x,y] = [154, 205, 50]
                  #  landClassification[x, y]= "Minor Veg"
                elif NDVI <0.25 and NDVI>0.1:
                    img[x,y] = [60,60,60]
                    landClassification[x, y] = "Urban"
               # elif NDVI<0.01 and NDVI>0:
                #    img[x,y] = [255,255,255]
                else:
                    landClassification[x, y] = "Unclassifed"

    save(filepath+"/data.npy",landClassification)
    cv2.imwrite(filepath+"/classification.png",img)

#Reshape the Image
def reshapeImage(path,RED,NIR):
    commandBand3 = "gdalwarp -t_srs EPSG:3857 -te -13784347.9328 6172442.9081 -13714025.8668 6253160.4100 " + RED + " " +path + "/RED.TIF"
    commandBand4 = "gdalwarp -t_srs EPSG:3857 -te -13784347.9328 6172442.9081 -13714025.8668 6253160.4100 " + NIR + " " +path + "/NIR.TIF"
    os.system(commandBand3)
    os.system(commandBand4)

# Landsat 8 and Landsat 7 data
# Band 2 Blue
# Band 3 Green
# Band 4 Red
# Band 5 NIR
def getDataLocation(location):
    listofDir = os.listdir(dataLocation)
    for i in listofDir:
        bandsLocation = location + "/" + i
        listofBands = os.listdir(bandsLocation)
        fileLocationInList = 0
        band2 = 0
        band3 = 0
        band4 = 0
        bnad5 = 0
        for file in listofBands:
            if "B2.TIF" in file:
                band2 = listofBands[fileLocationInList]
                band2 = bandsLocation + "/" + band2
            if "B3.TIF" in file:
                band3 = listofBands[fileLocationInList]
                band3 = bandsLocation + "/" + band3
            if "B4.TIF" in file:
                band4 = listofBands[fileLocationInList]
                band4 = bandsLocation + "/" + band4
            if "B5.TIF" in file:
                band5 = listofBands[fileLocationInList]
                band5 = bandsLocation + "/" + band5
            fileLocationInList += 1
        readLandsatBands(bandsLocation, band2, band3, band4, band5)

if __name__ == '__main__':
    dataLocation = "/media/russell/775C-44EC/LandsatExport/Victoria/Landsat4-8"
    getDataLocation(dataLocation)
