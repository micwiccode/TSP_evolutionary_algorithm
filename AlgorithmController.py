from ChartController import ChartController
from Loader import Loader
from DeterministicAlgorithm import DeterministicAlgorithm
from RandomAlgorithm import RandomAlgorithm
from EvolutionAlgorithm import EvolutionAlgorithm
from Logger import Logger
import timeit


class AlgorithmController:

    def __init__(self, method, dataCollection):
        self.method = method
        self.dataCollection = dataCollection
        self.citiesList, self.edgeWeightType = Loader.loadFile(self.dataCollection)

    def startAlgorithm(self, numberOfGenerations, popSize, propCross, propMutate, tourSize, mutationType, crossType):
        global bestSolution, worstSolution, avg, sd, trailsLengths
        startTime = timeit.default_timer()
        if numberOfGenerations == 'N':
            numberOfGenerations = len(self.citiesList)

        if self.method == 'Metoda losowa':
            randomAlgorithm = RandomAlgorithm(self.citiesList, numberOfGenerations, self.edgeWeightType)
            trailsLengths, bestSolution, worstSolution, avg, sd = randomAlgorithm.start()
            ChartController.generateChart(trailsLengths, None, None, None)

        if self.method == 'Metoda zachłanna':
            deterministicAlgorithm = DeterministicAlgorithm(self.citiesList, numberOfGenerations, self.edgeWeightType)
            trailsLengths, bestSolution, worstSolution, avg, sd = deterministicAlgorithm.start()
            ChartController.generateChart(trailsLengths, None, None, None)

        if self.method == 'Algorytm ewolucyjny':
            evolutionAlgorithm = EvolutionAlgorithm(self.citiesList, numberOfGenerations, self.edgeWeightType, popSize,
                                                    propCross, propMutate, tourSize, mutationType, crossType)
            bestSolutions, worstSolutions, avgs, sds = evolutionAlgorithm.start()
            ChartController.generateChart(None, bestSolutions, worstSolutions, avgs)

            bestSolutions.sort()
            bestSolution = round(bestSolutions[0])
            worstSolutions.sort(reverse=True)
            worstSolution = round(worstSolutions[0])
            avg = round(sum(avgs) / len(avgs), 2)
            sd = round(sum(sds) / len(sds), 2)

        stopTime = timeit.default_timer()
        time = round((stopTime - startTime), 2)

        logger = Logger(self.method, self.dataCollection, numberOfGenerations, popSize, propCross, propMutate,
                        tourSize, mutationType, crossType, bestSolution, worstSolution, avg, sd, time)
        logger.logResults()
        logger.saveResultsInFile()

        return bestSolution, worstSolution, avg, sd, time
