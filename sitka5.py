import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")
csvfile = csv.reader(infile)
header_row = next(csvfile)

dvinfile = open("death_valley_2018_simple.csv", "r")
dvcsvfile = csv.reader(dvinfile)
dvheader_row = next(dvcsvfile)

maxtemp = header_row.index("TMAX")
mintemp = header_row.index("TMIN")
nameidx = header_row.index("NAME")
dateidx = header_row.index("DATE")

dvmaxtemp = dvheader_row.index("TMAX")
dvmintemp = dvheader_row.index("TMIN")
dvnameidx = dvheader_row.index("NAME")
dvdateidx = dvheader_row.index("DATE")

highs = []
lows = []
dates = []
dvhighs = []
dvlows = []
dvdates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(mydate)

for row in csvfile:
    highs.append(int(row[maxtemp]))
    lows.append(int(row[mintemp]))
    thedate = datetime.strptime(row[dateidx], "%Y-%m-%d")
    name = row[nameidx]
    dates.append(thedate)

for row in dvcsvfile:
    try:
        hightemp = int(row[dvmaxtemp])
        lowtemp = int(row[dvmintemp])
        dvdate = datetime.strptime(row[dvdateidx], "%Y-%m-%d")
        dvname = row[dvnameidx]
    except ValueError as err:
        print("There is an error in", row[dvdateidx])
    else:
        dvhighs.append(hightemp)
        dvlows.append(lowtemp)
        dvdates.append(dvdate)
        dvname = row[dvnameidx]

import matplotlib.pyplot as plt

fig = plt.figure()

# fig.autofmt_xdate()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red", alpha=0.7)
plt.plot(dates, lows, c="blue", alpha=0.7)
plt.fill_between(x=dates, y1=lows, y2=highs, facecolor="blue", alpha=0.1)
plt.title(name)


plt.subplot(2, 1, 2)
plt.plot(dvdates, dvhighs, c="red", alpha=0.7)
plt.plot(dvdates, dvlows, c="blue", alpha=0.7)
plt.fill_between(x=dvdates, y1=dvlows, y2=dvhighs, facecolor="blue", alpha=0.1)
plt.title(dvname)

fig.autofmt_xdate()


plt.suptitle("Temp Comparison Between" + " " + row[nameidx] + row[dvnameidx])

plt.show()
