import math

from ResultsAnalyzer import ResultsAnalyzer


class Algorithm:

    def __init__(self, citiesList, numberOfGenerations, edgeWeightType):
        self.citiesList = citiesList
        self.numberOfGenerations = int(numberOfGenerations)
        self.edgeWeightType = edgeWeightType
        self.trailsLengths = []
        self.resultsAnalyzer = ResultsAnalyzer()

    def start(self):
        pass

    def getTrailLength(self, trail):
        distance = 0.0
        if self.edgeWeightType == 'GEO':
            for i in range(len(trail) - 1):
                lat1 = self.citiesList[trail[i]][0]
                lon1 = self.citiesList[trail[i]][1]
                lat2 = self.citiesList[trail[i + 1]][0]
                lon2 = self.citiesList[trail[i + 1]][0]

                phi1, phi2 = math.radians(lat1), math.radians(lat2)
                dlat = math.radians(lat2 - lat1)
                dlon = math.radians(lon2 - lon1)

                a = math.sin(dlat / 2) ** 2 + \
                    math.cos(phi1) * math.cos(phi2) * math.sin(dlon / 2) ** 2

                distance += 2 * 6373 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        else:
            numberOfCities = len(self.citiesList)

            for i in range(numberOfCities - 1):
                distance += math.sqrt(
                    abs(self.citiesList[trail[i]][0] - self.citiesList[trail[i + 1]][0]) ** 2 + abs(
                        self.citiesList[trail[i]][1] - self.citiesList[trail[i + 1]][1]) ** 2)
            distance += math.sqrt(
                abs(self.citiesList[trail[0]][0] - self.citiesList[trail[numberOfCities - 1]][0]) ** 2 + abs(
                    self.citiesList[trail[0]][1] - self.citiesList[trail[numberOfCities - 1]][1]) ** 2)

        return distance
