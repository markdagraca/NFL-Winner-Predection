import numpy
import pandas

filename = "NFL 2018.xlsx"

file = pandas.read_excel(filename)
label = file.columns

features = []
featuresResults = []
testing = []

# Split the data into reference and testing data
for x in range(0, len(file[label])):
    temp = [file[label[1]][x], file[label[2]][x], file[label[3]][x], file[label[4]][x], file[label[5]][x],
            file[label[6]][x],
            file[label[7]][x],
            file[label[8]][x], file[label[9]][x]]
    if not numpy.isnan(file[label[12]][x]):
        features.append(temp)
        featuresResults.append([file[label[12]][x], file[label[13]][x]])
    elif not type(temp[0]) == float and not type(temp[6]) == float and not type(temp[7]) == float:
        testing.append(temp)


# generalize the teams by setting the away team to 0 and the home team to 100
def generalizeData(data):
    for x in range(0, len(data)):
        team1 = str.capitalize(data[x][0])
        team2 = str.capitalize(data[x][1])
        data[x][0] = 0
        data[x][1] = 100
        for i in range(0, len(data[x])):
            if type(data[x][i]) is str:
                if team1 == str.capitalize(data[x][i]):
                    data[x][i] = 0
                elif team2 == str.capitalize(data[x][i]):
                    data[x][i] = 100
            else:
                data[x][i] = int(data[x][i])


def getTeams(data):
    output = []
    for x in data:
        output.append([x[0], x[1]])
    return output


testingOutput = getTeams(testing)
generalizeData(testing)
generalizeData(features)

# Import five thirty eight historical dataset
import csv

five38csv = []
year = 1900

with open('nfl_elo.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = False
    for line in csv_reader:
        if not first:
            first = True
        else:
            if (int(line[1]) >= year and len(line[12])):
                features.append([0, 100, int(100 * float(line[8])), int(100 * float(line[9])),-1, -1, -1, -1, -1])
                featuresResults.append([int(line[12]), int(line[13])])

# Machine learning using K nearest neighbors regressor algorithm
from sklearn import neighbors
from sklearn import tree




machinelearning = neighbors.KNeighborsRegressor(7)
machinelearning = machinelearning.fit(features, featuresResults)
machinelearning = machinelearning.predict(testing)




for x in range(0, len(testingOutput)):
    print(testingOutput[x][0] + " VS " + testingOutput[x][1] + " " + str(int(machinelearning[x][0])) + " to "
          + str(int(machinelearning[x][1])) + " Diffrence is " + str(
        abs((machinelearning[x][1] - (machinelearning[x][0]))))[0:4])
print("")
for x in range(0, len(testingOutput)):
    if (machinelearning[x][0] < machinelearning[x][1]):
        print(testingOutput[x][1])
    else:
        print(testingOutput[x][0])

