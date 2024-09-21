import csv, datetime

def findProp(filePath):
    fh = open(filePath, "r")
    csvFile = csv.DictReader(fh)

    propDict = {}

    for row in csvFile:
        result = row["Status"]
        if result in propDict:
            propDict[result] += 1
        else:
            propDict[result] = 1

    fh.close()

    return propDict

import matplotlib.pyplot as py

pf = findProp("midterm2.csv")
f = list(pf.values())
r = list(pf.keys())

py.pie(f, labels=r, autopct="%1.1f%%")
py.show()