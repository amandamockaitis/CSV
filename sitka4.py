# 1) handle error checking using try and except
# 2) change file to use death valley data
import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(mydate)

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print("missing data for", row[2])
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)

# print(highs)
# print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.7)
plt.plot(dates, lows, c="blue", alpha=0.7)
plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)

# x then y axis

plt.title("Daily High and Low Temps - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
# ticks on both axis and just the major ones

fig.autofmt_xdate()

plt.show()
