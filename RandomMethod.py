import random


class RandomMethod:

    def runRandomMethod(citiesList):
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
