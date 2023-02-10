import pandas as pd
import matplotlib.pyplot as plt


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    if int(h) == 0:
        return int(m) * 60 + float(s) * 1
    return int(h) * 60 + int(m) * 1 + float(s) * .1

def listofsec(time_list):
    results = []
    for x in time_list:
        if (x != "nan" and x!= "DNR" and x!= "Bike" and x!= "320 goal " and x!= ""):
            print(x, get_sec(x))
            results.append(get_sec(x))
    return results

def Average(lst):
    return sum(lst) / len(lst)




#xls = pd.read_excel(r'C:\Users\patri\Desktop\2K Scores .xlsx')

xls = pd.ExcelFile(r'C:\Users\patri\Desktop\2K Scores .xlsx')
sheet1 = xls.parse(0)  #sheet11_15_2013
sheet2 = xls.parse(1)  #sheet12_13_2013  This sheet is no good. Abnormal Formatting
sheet3 = xls.parse(2)   #sheet2_10_2014
sheet4 = xls.parse(3)   #sheet2_17_2014
sheet5 = xls.parse(4)   #sheet2_24_2014
sheet6 = xls.parse(5)   #sheet3_24_2014
sheet7 = xls.parse(6)   #sheet2_16_2015
sheet8 = xls.parse(7)   #sheet2_23_2015
sheet9 = xls.parse(8)   #sheet3_24_2015
sheet10 = xls.parse(9)   #sheet3_27_2015
sheet11 = xls.parse(10) #sheet12_08_2015
sheet12 = xls.parse(11)  #sheet2_08_2016
sheet13 = xls.parse(12)  #sheet2_15_2016
sheet14 = xls.parse(13)  #sheet2_22_2016
sheet15 = xls.parse(14)  #sheet2_29_2016
sheet16 = xls.parse(15) #sheet11_12_2016




sheet1['Timestring'] = sheet1['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet1 = listofsec(sheet1['Timestring'])
#print(newsheet1)

sheet3['Timestring'] = sheet3['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet3 = listofsec(sheet3['Timestring'])
#print(newsheet1)

sheet4['Timestring'] = sheet4['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet4 = listofsec(sheet4['Timestring'])
#print(newsheet1)

sheet5['Timestring'] = sheet5['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet5 = listofsec(sheet5['Timestring'])
#print(newsheet1)

sheet6['Timestring'] = sheet6['Time'].astype(str)
#print(sheet6['Timestring'])
newsheet6 = listofsec(sheet6['Timestring'])
#print(newsheet6)

sheet7['Timestring'] = sheet7['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet7 = listofsec(sheet7['Timestring'])
#print(newsheet1)

sheet8['Timestring'] = sheet8['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet8 = listofsec(sheet8['Timestring'])
#print(newsheet1)

sheet9['Timestring'] = sheet9['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet9 = listofsec(sheet9['Timestring'])
#print(newsheet1)

sheet10['Timestring'] = sheet10['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet10 = listofsec(sheet10['Timestring'])
#print(newsheet1)

sheet11['Timestring'] = sheet11['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet11 = listofsec(sheet11['Timestring'])
#print(newsheet1)

sheet12['Timestring'] = sheet12['Time'].astype(str)
#print(sheet1['Timestring'])
newsheet12 = listofsec(sheet12['Timestring'])
#print(newsheet1)

sheet13['Timestring'] = sheet13['Time'].astype(str)
print(sheet13['Timestring'])
newsheet13 = listofsec(sheet13['Timestring'])
print(newsheet13)




sheet1Avg = Average(newsheet1)
sheet3Avg = Average(newsheet3)
sheet4Avg = Average(newsheet4)
sheet5Avg = Average(newsheet5)
sheet6Avg = Average(newsheet6)
sheet7Avg = Average(newsheet7)
sheet8Avg = Average(newsheet8)
sheet9Avg = Average(newsheet9)
sheet10Avg = Average(newsheet10)
sheet11Avg = Average(newsheet11)
sheet12Avg = Average(newsheet12)
sheet13Avg = Average(newsheet13)
#print(sheet1Avg)
# sheet3Avg = sheet3["Time"].mean()
# sheet4Avg = sheet4["Time"].mean()

x = [sheet1["Timestring"][0], sheet3["Timestring"][0], sheet4["Timestring"][0], sheet5["Timestring"][0], sheet6["Timestring"][0], sheet7["Timestring"][0], sheet8["Timestring"][0], sheet9["Timestring"][0], sheet10["Timestring"][0], sheet11["Timestring"][0], sheet12["Timestring"][0], sheet13["Timestring"][0]]
y = [sheet1Avg, sheet3Avg, sheet4Avg, sheet5Avg, sheet6Avg, sheet7Avg, sheet8Avg, sheet9Avg, sheet10Avg, sheet11Avg, sheet12Avg, sheet13Avg]

pairs = zip(x,y)
pairs = sorted(pairs, reverse=True)
print(sorted(pairs))

xx= [x[0] for x in pairs]
yy= [x[1] for x in pairs]

print("xx", xx)
print("yy",  yy)

plt.scatter(xx,yy)



# DF = pd.DataFrame()
# DF['value'] = y
# DF = DF.set_index(x)
# plt.plot(DF)
# plt.gcf().autofmt_xdate()
# plt.show()


plt.show()