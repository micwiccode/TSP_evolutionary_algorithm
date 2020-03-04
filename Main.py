import random
from math import sqrt


def loader():
    dataFile = open('TSP/berlin52.tsp', 'r')
    name = dataFile.readline().strip().split()[1]  # NAME
    fileType = dataFile.readline().strip().split()[1]  # TYPE
    comment = dataFile.readline().strip().split()[1]  # COMMENT
    dimension = dataFile.readline().strip().split()[1]  # DIMENSION
    edgeWeightType = dataFile.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
    dataFile.readline()

    # Read nodes
    citiesList = []
    for i in range(0, int(dimension)):
        x, y = dataFile.readline().strip().split()[1:]
        citiesList.append([float(x), float(y)])

    # Close input file
    dataFile.close()
    return citiesList


def randomMethod(citiesList):
    numberOfCities = len(citiesList)
    randomTrail = []
    visited = []

    for i in range(numberOfCities):
        cityIndex = int(random.uniform(0, 1) * numberOfCities)
        while cityIndex in visited:
            cityIndex = int(random.uniform(0, 1) * numberOfCities)
        randomTrail.append(citiesList[cityIndex])

    randomTrail.append(randomTrail[0])
    return randomTrail


def deterministicMethod(citiesList):
    currentCityIndex = 0
    trail = [citiesList[currentCityIndex]]
    visitedCitiesIndexes = [0]

    for i in range(len(citiesList) - 1):
        distances = []
        for cityIndex in range(len(citiesList)):
            if not (cityIndex in visitedCitiesIndexes):
                distances.append([sqrt(
                    abs(citiesList[currentCityIndex][0] - citiesList[cityIndex][0]) ** 2 + abs(
                        citiesList[currentCityIndex][1] - citiesList[cityIndex][1]) ** 2), cityIndex
                ])
        distances.sort()


        currentCityIndex = distances[0][1]
        visitedCitiesIndexes.append(currentCityIndex)
        trail.append(citiesList[currentCityIndex])
    trail.append(citiesList[0])
    return trail


def getTrailLength(randomTrail):
    distance = 0
    for i in range(len(randomTrail) - 2):
        distance += sqrt(
            abs(randomTrail[i][0] - randomTrail[i + 1][0]) ** 2 + abs(randomTrail[i][1] - randomTrail[i + 1][1]) ** 2)
    return distance


if __name__ == '__main__':
    citiesList = loader()

    trail = randomMethod(citiesList)
    print(trail)
    print(getTrailLength(trail))

    trail2 = deterministicMethod(citiesList)
    print(trail2)
    print(getTrailLength(trail2))
