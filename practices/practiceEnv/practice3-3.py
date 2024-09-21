import matplotlib.pyplot as py
import csv, datetime

# x = range(1,6)
# y =[4, 2, 5, 1, 6]
# py.plot(x,y)
# py.show()

def findSubTimes(fileName):
    fh = open(fileName, "r")
    csvFile = csv.DictReader(fh)
    subTimes = []
    for row in csvFile:
        dt = datetime.datetime.strptime(row["SubmissionTime"], "%H:%M:%S").time()
        sub = (dt.hour - 9) * 3600 + (dt.minute - 20) * 60 + dt.second
        subTimes.append(sub)
    return subTimes

endpoints = range(0, 12000, 1000)
subTimes = findSubTimes("midterm2.csv")
py.hist(subTimes, bins= endpoints, facecolor="grey", edgecolor="black", orientation="vertical")
py.ylim(0, 120)
py.xlim(0, 11000)
py.xlabel("Submission time")
py.ylabel("Frequency")
py.title("Histogram of submission times")
py.show()
