## Reading CSV File
list = []
import csv


with open("Gapminder_clean.csv", "r", encoding="utf-8-sig") as gapminder:
    reader = csv.reader(gapminder)
    for row in reader:
        list.append(row)

# print(list)
import numpy as np

arr1 = np.array(list)
# print(arr1)
ny = arr1[:, [0]]
# print(len(ny))
nr = np.unique(ny)
# print(nr)
list2 = nr
list2 = np.delete(list2, 48)
# print(list2)

arr1 = arr1[:, [0, 2, 7, 9, 10, 12,15, 40,  42]]
# print(len(arr1))
# print(arr1[0])
#print(arr1)
# print(len(arr1[0]))


arr3 = arr1[1:, 0:1]
# print(arr3)
# print(arr1)
arr7 = arr1[1:, 1:]
# print(arr7)
# arr7 = arr7.astype('float')
# print(arr7)
# print(arr3)
# Normalization


# from sklearn import preprocessing

# arr2 = preprocessing.normalize(arr7)
# print(arr2)

arr2 = np.append(arr3, arr2, axis=1)
# print(arr2)

dict = {}


def dataCountry(arr2, countryname):
    list1 = []
    for values in arr2:
        for item in values:
            if item == countryname:
                list1.append(values)
    return list1


for i in range(len(list2)):
    Countrydata = dataCountry(arr2, list2[i])
    # print(Countrydata)
    arr4 = np.array(Countrydata)
    arr4 = arr4[:, 1:]
    arr4 = arr4.astype('float')
    arr5 = arr4.mean(axis=0)
    # print(arr5)
    arr6 = arr5.sum()
    # print(arr6)
    print(list2[i],arr6)
    dict.setdefault(list2[i], arr6)
# print(dict)
import operator

sort = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
print(sort)
sort1 = np.array(sort)
dict1 = {}
for j in range(len(list2)):
	ram = np.where(sort1 == list2[j])
	#print(list2[j], ram[0])
	dict1.setdefault(list2[j], ram[0])
print(dict1)
import csv
rank = 0
with open("ranking.csv","w",newline="") as file2:
    fieldnames = ["Ranking","Country"]
    thewriter = csv.DictWriter(file2,fieldnames = fieldnames)
    thewriter.writeheader()
    for country in sort:
        rank = rank + 1
        thewriter.writerow({"Ranking":rank,"Country":country})