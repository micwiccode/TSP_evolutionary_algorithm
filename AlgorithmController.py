from Loader import Loader
from DeterministicAlgorithm import DeterministicAlgorithm
from RandomAlgorithm import RandomAlgorithm
from ResultsAnalyzer import ResultsAnalyzer
from ChartController import ChartController
import timeit


class AlgorithmController:

    def __init__(self, method, dataCollection):
        self.method = method
        self.dataCollection = dataCollection
        self.citiesList, self.edgeWeightType = Loader.loadFile(self.dataCollection)

    def startAlgorithm(self, iteretionsNumber):
        startTime = timeit.default_timer()
        trailsLengths = []
        if iteretionsNumber == 'N':
            iteretionsNumber = len(self.citiesList)

        if self.method == 'Metoda losowa':
            randomAlgorithm = RandomAlgorithm(self.citiesList, iteretionsNumber, self.edgeWeightType)
            trailsLengths = randomAlgorithm.start()

        if self.method == 'Metoda zachłanna':
            deterministicAlgorithm = DeterministicAlgorithm(self.citiesList, iteretionsNumber, self.edgeWeightType)
            trailsLengths = deterministicAlgorithm.start()

        stopTime = timeit.default_timer()
        time = round((stopTime - startTime), 2)
        ChartController.generateChart(trailsLengths)

        if len(trailsLengths) == 1:
            return round(trailsLengths[0], 2), round(trailsLengths[0], 2), round(trailsLengths[0], 2), round(
                trailsLengths[0], 2), time
        else:
            resultsAnalyzer = ResultsAnalyzer(trailsLengths)
            bestSolution = resultsAnalyzer.getBestSolution()
            worstSolution = resultsAnalyzer.getWorstSolution()
            avg = resultsAnalyzer.getAvg()
            sd = resultsAnalyzer.getSd()
            return bestSolution, worstSolution, avg, sd, time
