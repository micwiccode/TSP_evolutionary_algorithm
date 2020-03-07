from math import sqrt
import random


class DeterministicMethod:

    def runDeterministicMethod(citiesList, startCityIndex):
        currentCityIndex = startCityIndex
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
        trail.append(citiesList[startCityIndex])
        return trail
