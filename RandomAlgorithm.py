from random import randrange
from Algorithm import Algorithm


class RandomAlgorithm(Algorithm):

    def __init__(self, citiesList, numberOfGenerations, edgeWeightType):
        super().__init__(citiesList, numberOfGenerations, edgeWeightType)

    def start(self):
        super().start()
        for i in range(self.numberOfGenerations):
            trail = self.runRandomMethod()
            self.trailsLengths.append(self.getTrailLength(trail))
        return self.resultsAnalyzer.analiseResult(self.trailsLengths)

    def runRandomMethod(self):
        numberOfCities = len(self.citiesList)
        startCityIndex = randrange(numberOfCities)
        visitedCitiesIndexes = [startCityIndex]
        trail = [startCityIndex]

        for i in range(numberOfCities-1):
            nextCityIndex = randrange(numberOfCities)
            while nextCityIndex in visitedCitiesIndexes:
                nextCityIndex = randrange(numberOfCities)
            trail.append(nextCityIndex)
            visitedCitiesIndexes.append(nextCityIndex)

        return trail
