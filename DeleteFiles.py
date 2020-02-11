import os


#Run this to delete all the older RED.TIF and NIR.TIF files to
#allow to be freshly created
def getDataLocation(location):
    listofDir = os.listdir(dataLocation)
    for i in listofDir:
        bandsLocation = location + "/" + i
        listofBands = os.listdir(bandsLocation)
        fileLocationInList = 0
        for file in listofBands:
            if "RED.TIF" == file:
                band2 = bandsLocation + "/RED.TIF"
                os.remove(band2)
            if "NIR.TIF" in file:
                band3 = bandsLocation + "/NIR.TIF"
                os.remove(band3)


if __name__ == '__main__':
    dataLocation = "/media/russell/775C-44EC/LandsatExport/Victoria/Landsat4-8"
    getDataLocation(dataLocation)
