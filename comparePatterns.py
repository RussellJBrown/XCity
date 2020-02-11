import os
import sys
import numpy as np
import serial
from numpy import save


'''
There are several different ways pixels can form.
Water will remain relatively constant in terms of a time series analysis, besides
vegetation on the surface of the water.
The main changes will be expected to be seen in with

'''
def compareHowModelsChange(pixelModels):
    listOfModels = os.listdir(pixelModels)
    count = 0

    #Used for all Models
    models = []
    modelFrequency = []

    modelTransformation = {}
    modelStagnant = {}
    previousModelD = {}

    previousModels = []

    notFirstModel = 0
    for i in listOfModels:
        data =  np.load(pixelModels+"/"+i,allow_pickle=True)
        row=data.shape[0]
        col=data.shape[1]
        print("New Model:")
        print(row)
        print(col)
        #The first if stament, creates the inital set of models
        #Loads current model in the proper array
        if notFirstModel==0:
            notFirstModel+=1
            for x in range(row):
                for y in range(col):
                    currentModel = data[x,y]
                    previousModels.append(currentModel)

                    if currentModel not in models:
                        models.append(currentModel)
                        modelFrequency.append(1)

                    else:
                        index = models.index(currentModel)
                        modelFrequency[index]+=1
            previousModelNP = np.asarray(previousModels, dtype=object)


        #Comparing aganist how models change over time
        #This portion is reached if models are all found
        #
        #Looks how frequent one model compares to a different model
        #
        else:
            countForPreviousModel=0
            currentModelMax = row*col
            try:
                if currentModelMax>len(previousModels):
                    currentModelMax=previousModelNP.size[0]
            except:
                    pass
            previousModels=[]
            for x in range(row):
                for y in range(col):
                    currentModel = data[x,y]
                    previousModels.append(currentModel)
                    compare=["","","","",""]
                    if countForPreviousModel<len(previousModelNP):
                        compare = previousModelNP[countForPreviousModel].tolist()
                        countForPreviousModel+=1
                    #If a model does not exist add it.
                    #Mark how the previous version changed.
                    if currentModel not in models:
                        models.append(currentModel)
                        modelFrequency.append(1)
                    #Check how previous model changed
                    #if collections.Counter(currentModel) == collections.Counter(models):
                    else:
                        index = models.index(currentModel)
                        modelFrequency[index]+=1
                    if compare!=currentModel:
                        transformation=[]
                        transformation.extend(compare)
                        transformation.append("->")
                        transformation.extend(currentModel)
                        transformationS = ""

                        try:
                            transformationS = transformationS.join(transformation)
                        except:
                            pass

                        #Tests to see if new Transformation
                        #if new add new transformation
                        if transformationS in modelTransformation.keys():
                            modelTransformation[transformationS]+=1
                        else:
                            modelTransformation[transformationS]=1
                            pass
                    #This statement gets reached
                    #means the location has stayed the same
                    else:
                        stagnant = []
                        stagnant.extend(compare)
                        stagnant.append("->")
                        stagnant.extend(currentModel)
                        stagnantS=""
                        try:
                            stagnantS = stagnantS.join(stagnant)
                        except:
                            pass

                        #If Transformation is recorded if it isn't
                        if stagnantS in modelStagnant.keys():
                            modelStagnant[stagnantS]+=1
                            #print("Increased")
                        #Add count to position in stagnant
                        else:
                            modelStagnant[stagnantS]=1
                            #print("added")
            previousModelNP = np.asarray(previousModels, dtype=object)


    print("Model Transformation: ")
    print(modelTransformation)
    print("Model Stagnant: ")
    print(modelStagnant)

if __name__ == '__main__':
    patterenLocation = "/media/russell/775C-44EC/Models/Victoria"
    compareHowModelsChange(patterenLocation)
