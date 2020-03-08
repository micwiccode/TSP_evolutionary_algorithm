from random import randrange
from Algorithm import Algorithm


class RandomAlgorithm(Algorithm):

    def __init__(self, citiesList, iteretionsNumber, edgeWeightType):
        super().__init__(citiesList, iteretionsNumber, edgeWeightType)

    def start(self):
        super().start()
        for i in range(int(self.iteretionsNumber)):
            trail = self.runRandomMethod()
            self.trailsLengths.append(self.getTrailLength(trail))
        return self.trailsLengths

    def runRandomMethod(self):
        numberOfCities = len(self.citiesList)
        startCityIndex = randrange(numberOfCities)
        visitedCitiesIndexes = [startCityIndex]
        trail = [self.citiesList[startCityIndex]]

        for i in range(numberOfCities-1):
            nextCityIndex = randrange(numberOfCities)
            while nextCityIndex in visitedCitiesIndexes:
                nextCityIndex = randrange(numberOfCities)
            trail.append(self.citiesList[nextCityIndex])
            visitedCitiesIndexes.append(nextCityIndex)

        trail.append(self.citiesList[startCityIndex])
        return trail
