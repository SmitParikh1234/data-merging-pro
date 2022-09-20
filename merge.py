import csv
dataset1 = []
dataset2 = []
with open("bright_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open("dwarf_stars.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
headers1 = dataset1[0]
planetdata1 = dataset1[1:]
headers2 = dataset2[0]
planetdata2 = dataset2[1:]
headers = headers1+headers2
planetdata = []
for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

solar_mass = []
for index,data in  enumerate(planetdata1[6]):
  solar_mass.append(planetdata1[6][index]*0.000954588)

planetdata.append(solar_mass)

solar_radius = []
for index,data in  enumerate(planetdata1[7]):
  solar_radius.append(planetdata1[7][index]*0.102763)

planetdata.append(solar_radius)

with open("merge.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)