import statistics


class ResultsAnalyzer:

    def __init__(self, trailsLengths):
        self.trailsLengths = trailsLengths

    def getBestSolution(self):
        self.trailsLengths.sort()
        return round(self.trailsLengths[0])

    def getWorstSolution(self):
        self.trailsLengths.sort(reverse=True)
        return round(self.trailsLengths[0])

    def getAvg(self):
        return round(sum(self.trailsLengths) / len(self.trailsLengths), 2)

    def getSd(self):
        return round(statistics.stdev(self.trailsLengths), 2)
