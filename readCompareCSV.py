import csv
import os

""" with open("CargosMensual20211USUARIA.csv", "r",) as t1, open("CargosMensual20211_1.csv", "r") as t2:
    fileUserPac = list(csv.reader(t1, delimiter=";"))
    filePac = list(csv.reader(t2, delimiter=";"))
    outFile = open("./outNotFound.txt", "w")

    notFounded = []

    for lineUP in fileUserPac:
        if (lineUP not in filePac):
            listToStr = ''.join((map(str, lineUP)))+'\n'
            outFile.write(listToStr)
            notFounded.append(lineUP)

outFile.close() """


def getIndexesArray(file):
    indexArray = []
    for line in file:
        indexArray.append(line[0])
    return indexArray


with open("file1.csv", "r",) as t1, open("file2.csv", "r") as t2:
    fileUserPac = list(csv.reader(t1, delimiter=";"))
    filePac = list(csv.reader(t2, delimiter=";"))
    indexesArrayUserPac = getIndexesArray(fileUserPac)
    indexesArrayPac = getIndexesArray(filePac)
outFile = open("./outNotFound.txt", "w")
notFounded = []
for lineUP in indexesArrayUserPac:
    if (lineUP not in indexesArrayPac):
        
        listToStr = ''.join((map(str, lineUP)))+'\n'
        outFile.write(listToStr)
        notFounded.append(lineUP)

outFile.close()
