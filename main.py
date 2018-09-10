import numpy
import pandas
from sklearn import tree

filename = "NFL 2018.xlsx"

file = pandas.read_excel(filename)
label = file.columns

features = []
featuresResults = []
testing = []

# Split the data into reference and testing data
for x in range(0, len(file[label])):
    temp = [file[label[1]][x], file[label[2]][x], file[label[3]][x], file[label[4]][x], file[label[5]][x],
            file[label[6]][x], file[label[7]][x],
            file[label[8]][x], file[label[9]][x]]
    if not numpy.isnan(file[label[11]][x]):
        features.append(temp)
        featuresResults.append([file[label[11]][x], file[label[12]][x]])
    else:
        testing.append(temp)


# generalize the teams by setting the away team to 1 and the home team to 2
def generalizeData(data):
    for x in range(0, len(data)):
        team1 = str.capitalize(data[x][0])
        team2 = str.capitalize(data[x][1])
        data[x][0] = 1
        data[x][1] = 2
        for i in range(0, len(data[x])):
            if type(data[x][i]) is str:
                if team1 == str.capitalize(data[x][i]):
                    data[x][i] = 1
                elif team2 == str.capitalize(data[x][i]):
                    data[x][i] = 2
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


from sklearn import neighbors
machinelearning=neighbors.KNeighborsRegressor()
machinelearning=machinelearning.fit(features,featuresResults)
machinelearning=machinelearning.predict(testing)


for x in range(0,len(testingOutput)):
    total=machinelearning[x][1]+machinelearning[x][0]
    home=int (machinelearning[x][0]/total*100)
    away=int (machinelearning[x][1]/total*100)


    print(testingOutput[x][0] +" VS " + testingOutput[x][1] +" " + str(int(machinelearning[x][0])) +" to "
          + str(int(machinelearning[x][1]))+" "+ str(home) +" vs "+ str(away))