import pickle
import numpy as np

#This file reads in the Stats Calculated in
#findNewModel.py
def createPredictedMap(dictS, dictT, npyBand, path):

    pickleT = open(dictT,"rb")
    TransPickle = pickle.load(pickleT)
    pickleT.close()

    pickleS = open(dictS,"rb")
    StagPickle = pickle.load(pickleS)
    pickleS.close()

    TransPickleL = list(TransPickle)
    StagPickleL = list(StagPickle)

    data = np.load(npyBand,allow_pickle=True)
    row = data.shape[0]
    col = data.shape[1]

    for i in range(0,row):
        for j in range(0,col):
            landClassification = data[i,j]
            landClassification = ', '.join(landClassification)

            for key in TransPickle:
                table = key.split("->")
                oldLocation = table[0]

                print("Current Pixel: ")
                print((oldLocation))

                print("Land Classification: ")
                print((landClassification))
                if oldLocation == landClassification:
                    print("intial bit found Trans")

            print("Finished Checking test 1")
            for key in StagPickle:
                table = key.split("->")
                #if table[0] == landClassification:
                #    print("intial bit found Stag")



def testPrint(StatSPath,StatTPath):
    pickleT = open(StatTPath,"rb")
    TransPickle = pickle.load(pickleT)
    pickleT.close()
    TransPickle = list(TransPickle.keys())
    for key in TransPickle:
        table = key.split("->")
        print(table[0])



def testPrintNP(numpyLocation):
    data = np.load(npyBand,allow_pickle=True)
    row = data.shape[0]
    col = data.shape[1]
    for i in range(0,row):
        for j in range(0,col):
            landClassification = data[i,j]
            landClassification = ', '.join(landClassification)
            print(landClassification)






if __name__ == '__main__':
    StatSPath = "/media/russell/775C-44EC/Models/Victoria/stagStats.p"
    StatTPath = "/media/russell/775C-44EC/Models/Victoria/transStats.p"
    #Currently hard coded in
    npyBand = "/media/russell/775C-44EC/Models/Victoria/data31.npy"
    path = "/media/russell/775C-44EC/Models/Victoria/"
    createPredictedMap(StatSPath, StatTPath, npyBand, path)
    #testPrint(StatSPath,StatTPath)
    #testPrintNP(npyBand)
