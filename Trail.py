from math import sqrt


class Trail:

    def getTrailLength(randomTrail):
        distance = 0
        for i in range(len(randomTrail) - 2):
            distance += sqrt(
                abs(randomTrail[i][0] - randomTrail[i + 1][0]) ** 2 + abs(
                    randomTrail[i][1] - randomTrail[i + 1][1]) ** 2)
        return distance
