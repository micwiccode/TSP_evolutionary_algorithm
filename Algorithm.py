import math


class Algorithm:

    def __init__(self, citiesList, iteretionsNumber, edgeWeightType):
        self.citiesList = citiesList
        self.iteretionsNumber = iteretionsNumber
        self.edgeWeightType = edgeWeightType
        self.trailsLengths = []

    def start(self):
        pass

    def getTrailLength(self, trail):
        distance = 0.0
        if self.edgeWeightType == 'GEO':
            for i in range(len(trail) - 1):
                lat1 = trail[i][0]
                lon1 = trail[i][1]
                lat2 = trail[i + 1][0]
                lon2 = trail[i + 1][1]

                phi1, phi2 = math.radians(lat1), math.radians(lat2)
                dlat = math.radians(lat2 - lat1)
                dlon = math.radians(lon2 - lon1)

                a = math.sin(dlat / 2) ** 2 + \
                    math.cos(phi1) * math.cos(phi2) * math.sin(dlon / 2) ** 2

                distance += 2 * 6373 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        else:
            for i in range(len(trail) - 1):
                distance += math.sqrt(
                    abs(trail[i][0] - trail[i + 1][0]) ** 2 + abs(
                        trail[i][1] - trail[i + 1][1]) ** 2)

        return distance
