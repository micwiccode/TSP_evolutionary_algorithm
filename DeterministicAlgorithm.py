from math import sqrt
from Algorithm import Algorithm


class DeterministicAlgorithm(Algorithm):

    def __init__(self, citiesList, numberOfGenerations, edgeWeightType):
        super().__init__(citiesList, numberOfGenerations, edgeWeightType)

    def start(self):
        super().start()
        for i in range(self.numberOfGenerations):
            trail = self.runDeterministicMethod(i % len(self.citiesList))
            self.trailsLengths.append(self.getTrailLength(trail))
        return self.resultsAnalyzer.analiseResult(self.trailsLengths)

    def runDeterministicMethod(self, startCityIndex):
        numberOfCities = len(self.citiesList)
        currentCityIndex = startCityIndex
        visitedCitiesIndexes = [startCityIndex]
        trail = [startCityIndex]

        for i in range(numberOfCities-1):
            distances = []
            for cityIndex in range(numberOfCities):
                if not (cityIndex in visitedCitiesIndexes):
                    distances.append([sqrt(
                        abs(self.citiesList[currentCityIndex][0] - self.citiesList[cityIndex][0]) ** 2 + abs(
                            self.citiesList[currentCityIndex][1] - self.citiesList[cityIndex][1]) ** 2), cityIndex
                    ])
            distances.sort()
            currentCityIndex = distances[0][1]
            visitedCitiesIndexes.append(currentCityIndex)
            trail.append(currentCityIndex)

        return trail
