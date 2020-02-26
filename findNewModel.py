import gdal
import pickle
import os
import sys

def findNewPattern(locationT,locationS,locationA,path):
    pickleT = open(locationT,"rb")
    TransPickle = pickle.load(pickleT)
    pickleT.close()

    pickleS = open(locationS,"rb")
    StagPickle = pickle.load(pickleS)
    pickleS.close()

    pickleA = open(locationA,"rb")
    AllPickle = pickle.load(pickleA)
    pickleA.close()

    dictAStatsT = AllPickle
    dictAStatsS = AllPickle

    keysT = list(TransPickle.keys())
    keysS = list(StagPickle.keys())
    A = list(AllPickle.keys())

    for key in A:
        #print(key)
        #print("\n")
        dictAStatsS[key] = 0
        dictAStatsT[key] = 0
        if key in TransPickle:
            updateValue = TransPickle[key]
            dictAStatsT[key] = updateValue

        if key in StagPickle:
            updateValue = StagPickle[key]
            dictAStatsS[key] = updateValue



    print("Writing Files")

    with open(path+"/transStats.p",'wb') as fp:
        pickle.dump(dictAStatsT, fp, protocol=pickle.HIGHEST_PROTOCOL)



    with open(path+"/stagStats.p","wb") as fp:
        pickle.dump(dictAStatsS,fp,protocol=pickle.HIGHEST_PROTOCOL)
    print("Finshed Writing Files")


#Test Method
def checkprint(DictT,DictS,DictA,Path):
    pickleT = open(DictT,"rb")
    TransPickle = pickle.load(pickleT)
    pickleT.close()

    pickleS = open(DictS,"rb")
    StagPickle = pickle.load(pickleS)
    pickleS.close()

    picklesA = open(DictA,"rb")
    AllPickle = pickle.load(picklesA)
    picklesA.close()

    print(TransPickle.items())
    print("")
    #print(StagPickle.items())
    #print("")
    #print(AllPickle.items())

if __name__ == '__main__':
    DictT = "/media/russell/775C-44EC/Models/Victoria/transPickle.p"
    DictS= "/media/russell/775C-44EC/Models/Victoria/stagPickle.p"
    DictA = "/media/russell/775C-44EC/Models/Victoria/mod.p"
    Path = "/media/russell/775C-44EC/Models/Victoria"
    findNewPattern(DictT,DictS,DictA,Path)
    #checkprint(DictT,DictS,DictA,Path)
