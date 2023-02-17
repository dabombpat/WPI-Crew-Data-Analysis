from math import floor

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas._libs import NaTType


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    if int(h) == 0:
        return int(m) * 60 + float(s) * 1
    return int(h) * 60 + int(m) * 1 + float(s) * .1


def listofsec(time_list):
    results = []
    for x in time_list:
        if ":" not in x:
            continue
        secs = get_sec(x)
        results.append(secs)
    return results


def timestamp_to_float(time: str) -> float:
    try:
        hours, minutes, seconds = [float(value) for value in time.split(":")]
        hours *= 3600
        minutes *= 60

        seconds += (hours + minutes)
        return seconds
    except ValueError:
        print(time)


def float_to_timestamp(seconds: float) -> str:
    hours = floor(seconds / 3600)
    seconds -= (hours * 3600)
    minutes = floor(seconds / 60)
    seconds -= (minutes * 60)

    return f"{minutes:02d}:{seconds:.2f}"


def Average(lst):
    num = [isinstance(x, float) for x in lst]
    return sum([x for x in lst if isinstance(x, float)]) / sum(num)


# xls = pd.read_excel(r'C:\Users\patri\Desktop\2K Scores .xlsx')

xls = pd.ExcelFile(r'C:\Users\patri\Desktop\2K Scores PAT.xlsx')
num_sheets = len(xls.sheet_names)
sheets = [xls.parse(x) for x in range(num_sheets)][:-1]

averages = []

for sheet in sheets:
    seconds_per_sheet = []
    sheet['Timestring'] = sheet['Time'].astype(str)

    seconds_per_sheet += listofsec(sheet['Timestring'])
    averages.append(Average(seconds_per_sheet))

x = []
y = []

for sheet, average in zip(sheets, averages):
    x.append(float("{:.2f}".format(timestamp_to_float(sheet['Timestring'][0]))))
    y.append(average)

# print(sheet1Avg)
# sheet3Avg = sheet3["Time"].mean()
# sheet4Avg = sheet4["Time"].mean()


pairs = zip(x, y)
pairs = sorted(pairs, reverse=True)
print(f"{pairs=}")

print(f"{x=}")
print(f"{y=}")


xx = [i[0] for i in pairs]
yy = [i[1] for i in pairs]

print(f"{xx=}")
print(f"{yy=}")

#LINE OF BEST FIT
xbar = sum(xx)/len(xx)
ybar = sum(yy)/len(yy)
n = len(xx)

numer = sum([xi*yi for xi,yi in zip(xx, y)]) - n * xbar * ybar
denum = sum([xi**2 for xi in xx]) - n * xbar**2

b = numer/denum

a = ybar - b * xbar
yfit = [a + b * xi for xi in xx]
# plt.plot(xx,yfit)

#LINE OF BEST FIT END
plt.scatter(xx, yy)

plt.xscale("linear")
# plt.xticks(xx, [float_to_timestamp(stamp) for stamp in xx], rotation=20)
# plt.yticks(yy, [float_to_timestamp(stamp) for stamp in yy])


# DF = pd.DataFrame()
# DF['value'] = y
# DF = DF.set_index(x)
# plt.plot(DF)
# plt.gcf().autofmt_xdate()
# plt.show()


plt.show()
