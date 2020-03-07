from math import sqrt
import statistics


class TrailCalculator:

    def getTrailLength(randomTrail):
        distance = 0
        for i in range(len(randomTrail) - 2):
            distance += sqrt(
                abs(randomTrail[i][0] - randomTrail[i + 1][0]) ** 2 + abs(
                    randomTrail[i][1] - randomTrail[i + 1][1]) ** 2)
        return distance

    def getBestSolution(trailsLengths):
        trailsLengths.sort()
        return round(trailsLengths[0])

    def getWorstSolution(trailsLengths):
        trailsLengths.sort(reverse=True)
        return round(trailsLengths[0])

    def getAvg(trailsLengths):
        return round(sum(trailsLengths) / len(trailsLengths), 2)

    def getSd(trailsLengths):
        return round(statistics.stdev(trailsLengths), 2)
