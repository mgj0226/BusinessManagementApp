import matplotlib.pyplot as py
import csv, datetime

def findSubCnt(fileName):
    fh = open(fileName, "r")
    csvFile = csv.DictReader(fh)
    subCntDict = {}
    for row in csvFile:
        sid = int(row["StudentID"])
        if sid in subCntDict:
            subCntDict[sid] += 1
        else:
            subCntDict[sid] = 1
    fh.close()
    return subCntDict

subCnt = findSubCnt("midterm2.csv")
seq = range(0, len(subCnt))
py.bar(seq, sorted(subCnt.values()), facecolor="grey", edgecolor="black", width=0.35)
py.show()