import h5py as H5F
import os
import sys
import numpy as np
import serial
from numpy import save

def analysisData(location):
    listofDir = os.listdir(location)
    count = 0
    for i in listofDir:
        npyBand = location + "/" + i
        listofBands = os.listdir(npyBand)
        for file in listofBands:
            if ".npy" in file:
                data = np.load(npyBand+"/"+file,allow_pickle=True)
                numrows = data.shape[0]
                numcols = data.shape[1]
                surroundingPixels = np.empty((numrows,numcols),dtype=object)
                for x in range(0,numrows):
                    for y in range(0,numcols):
                        landClassification = data[x,y]
                        northPixel=""
                        eastPixel=""
                        southPixel=""
                        westPixel=""
                        allLocations = []
                        allLocations.append(landClassification)
                        if x!=0:
                            northPixel=data[x-1,y]
                        if y!=0:
                            eastPixel=data[x,y-1]
                        if x!=numrows-1:
                            southPixel=data[x+1,y]
                        if y!=numcols-1:
                            westPixel=data[x,y+1]
                        allLocations.append(northPixel)
                        allLocations.append(eastPixel)
                        allLocations.append(southPixel)
                        allLocations.append(westPixel)
                        surroundingPixels[x,y] = allLocations

                modelsPath = "/media/russell/775C-44EC/Models/Victoria/"
                save(modelsPath+"/data"+str(count)+".npy",surroundingPixels)
                count+=1


if __name__ == '__main__':
    dataLocation = "/media/russell/775C-44EC/LandsatExport/Victoria/Landsat4-8"
    analysisData(dataLocation)
