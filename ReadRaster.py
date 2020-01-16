import os
#from pyrsgis import raster
#from pyrsgis.convert import changeDimension
from PIL import Image
from sklearn.model_selection import train_test_split
import numpy as np
from osgeo import gdal

def extractData():
    dataLocation = "/home/russell/XCity/Output"
    numpyTrueColourListB2 = []
    numpyTrueColourListB3 = []
    numpyTrueColourListB4 = []

    numpyFalseColourListB3 = []
    numpyFalseColourListB4 = []
    numpyFalseColourListB8 = []

    #Retrieves all the values
    for file in os.listdir(dataLocation):
        dataset = gdal.Open(dataLocation+"/"+file)
        if "TrueColor" in file:
            band2TrueColour =  np.array(dataset.GetRasterBand(1).ReadAsArray())
            numpyTrueColourListB2.append(band2TrueColour)
            band3TrueColour =  np.array(dataset.GetRasterBand(2).ReadAsArray())
            numpyTrueColourListB3.append(band3TrueColour)
            band4TrueColour =  np.array(dataset.GetRasterBand(3).ReadAsArray())
            numpyTrueColourListB4.append(band4TrueColour)

        if "FalseColor" in file:
            band3FalseColour =  np.array(dataset.GetRasterBand(1).ReadAsArray())
            numpyFalseColourListB3.append(band3FalseColour)
            band4FalseColour =  np.array(dataset.GetRasterBand(2).ReadAsArray())
            numpyFalseColourListB4.append(band4FalseColour)
            band8FalseColour =  np.array(dataset.GetRasterBand(3).ReadAsArray())
            numpyFalseColourListB8.append(band8FalseColour)
    return (numpyTrueColourListB2,numpyTrueColourListB3,numpyTrueColourListB4,numpyFalseColourListB3,numpyFalseColourListB4,numpyFalseColourListB8)


if __name__ == '__main__':
    extractData()
