import statistics
from ChartController import ChartController


class ResultsAnalyzer:

    def __init__(self):
        self.trailsLengths = []

    def analiseResult(self, trailsLengths):
        self.trailsLengths = trailsLengths.copy()
        bestSolution = self.getBestSolution()
        worstSolution = self.getWorstSolution()
        avg = self.getAvg()
        sd = self.getSd()
        return trailsLengths, bestSolution, worstSolution, avg, sd

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
