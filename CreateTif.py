
from glob import glob
import os
import rasterio
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
            if "B03_10m.jp2" in file:
                band3 = rasterio.open(filePath, driver='JP2OpenJPEG') #green
            if "B04_10m.jp2" in file:
                band4 = rasterio.open(filePath, driver='JP2OpenJPEG') #red
            if "B08_10m.jp2" in file:
                band8 = rasterio.open(filePath, driver='JP2OpenJPEG') #nir


        trueColourName='/home/russell/XCity/Output/TrueColor' + str(trueColourCount) + ".tiff"
        falseColourName='/home/russell/XCity/Output/FalseColor' + str(falseColourCount)+ ".tiff"
        trueColourCount+=1
        falseColourCount+=1

        print("Creating True Colour Tiff Image")
        trueColor = rasterio.open(trueColourName,'w',driver='Gtiff',
                                 width=band4.width, height=band4.height,
                                 count=3,
                                 crs=band4.crs,
                                 transform=band4.transform,
                                 dtype=band4.dtypes[0]
                                 )
        trueColor.write(band2.read(1),3) #blue
        trueColor.write(band3.read(1),2) #green
        trueColor.write(band4.read(1),1) #red
        trueColor.close()



        print("Creating False Colour Image")
        falseColor = rasterio.open(falseColourName, 'w', driver='Gtiff',
                          width=band2.width, height=band2.height,
                          count=3,
                          crs=band2.crs,
                          transform=band2.transform,
                          dtype='uint16'
                         )
        falseColor.write(band3.read(1),3) #Blue
        falseColor.write(band4.read(1),2) #Green
        falseColor.write(band8.read(1),1) #Red
        falseColor.close()
