import os
import sys
import numpy as np
import serial
from numpy import save
import csv
import pickle




def checkIfNew(modS,dictionary):

    if modS in dictionary.keys():
        dictionary[modS]+=1
    else:
        dictionary[modS]=1
    return dictionary

def stringCreator(compare,currentModel):
        compare = [xstr(s) + ", " for s in compare]
        currentModel = [xstr(s) + ", " for s in currentModel]
        mod=[]
        mod.extend(compare)
        mod.append("->, ")
        mod.extend(currentModel)
        modS = ""
        transformationS=""
        stagnantS=""
        modSJoin = False
        try:
            modS = modS.join(mod)
            return modS
        except:
            return False


'''
There are several different ways pixels can form.
Water will remain relatively constant in terms of a time series analysis, besides
vegetation on the surface of the water.
The main changes will be expected to be seen in with

'''
def compareHowModelsChange(pixelModels):
    listOfModels = os.listdir(pixelModels)
    #Used for all Models
    modelFrequency = []
    modelTransformation = {}
    modelStagnant = {}
    previousModelD = {}
    previousModels = []
    modAll = {}
    notFirstModel = 0

    #Read in List of Models
    for i in listOfModels:
        row = 0
        col = 0
        #Reading in the pixel maps in the proper order
        data =  np.load(pixelModels+"/"+i,allow_pickle=True)
        try:
            row=data.shape[0]
            col=data.shape[1]
        except:
            pass
        print("New Model:")
        print(row)
        print(col)


        #The first if stament, creates the inital set of models
        #Loads current model in the proper array
        if row > 0:

            #Loads the data into the previousModelNP
            if notFirstModel==0:
                notFirstModel+=1
                for x in range(row):
                    for y in range(col):
                        previousModels.append(data[x,y])
                previousModelNP = np.asarray(previousModels, dtype=object)



            #Comparing aganist how models change over time
            #This portion is reached if models are all found
            #
            #Looks how frequent one model compares to a different model
            #
            else:
                countForPreviousModel = 0
                previousModels=[]
                for x in range(row):
                    for y in range(col):
                        currentModel = data[x,y]
                        compare=["","","","",""]
                        try:
                            if countForPreviousModel<len(previousModelNP):
                                compare = previousModelNP[countForPreviousModel].tolist()
                                countForPreviousModel+=1
                        except:
                            pass

                        modS = stringCreator(compare,currentModel)
                        if modS != False:
                            modAll = checkIfNew(modS,modAll)
                            if compare!=currentModel:
                                #print("Adding to Transformation")
                                modelTransformation = checkIfNew(modS,modelTransformation)
                            else:
                                #print("Adding to Stag")
                                modelStagnant = checkIfNew(modS,modelStagnant)

                            previousModels.append(currentModel)
                previousModelNP = np.asarray(previousModels, dtype=object)

    print("Writing")
    with open(pixelModels+"/transPickle.p",'wb') as fp:
        pickle.dump(modelTransformation, fp, protocol=pickle.HIGHEST_PROTOCOL)

    with open(pixelModels+"/stagPickle.p","wb") as fp:
        pickle.dump(modelStagnant,fp,protocol=pickle.HIGHEST_PROTOCOL)

    with open(pixelModels+"/mod.p","wb") as fp:
        pickle.dump(modAll,fp,protocol=pickle.HIGHEST_PROTOCOL)


def xstr(s):
    if s is None:
        return ''
    return s



if __name__ == '__main__':
    patterenLocation = "/media/russell/775C-44EC/Models/Victoria"
    compareHowModelsChange(patterenLocation)
