import matplotlib.pyplot as py
import csv, datetime

# open the file
f = open("ubike.csv", "r")
bike = {}
capacity = {}
count = {}

# processing the data
for row in csv.DictReader(f):
    if row["station"] == "Roosevelt & Xinsheng S. Intersection":
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if hour not in bike:
            bike[hour] = int(row["bike"])
            capacity[hour] = int(row["lot"])
            count[hour] = 1
        else:
            bike[hour] += int(row["bike"])
            capacity[hour] += int(row["lot"])
            count[hour] += 1
f.close()

# preparing for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []
lot = []
for k in time_seq:
    avg.append(float(bike[k]) / count[k])
    lot.append(float(capacity[k]) / count[k])

# plotting the data in avg and lot
py.plot(time_seq, lot, label = "Average")
py.plot(time_seq, avg, label = "Capacity")
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
py.ylim(0, max(lot) + 30)
# py.ylim(0, max(avg) + 30)
# py.ylim(0, max(lot) * 1.2)
# set sequence of x-axis from 0 to 23 one by one
seq = range(0, 24, 1)
py.xticks(seq)
py.legend(loc="best")
py.show()