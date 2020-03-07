from Loader import Loader
from DeterministicMethod import DeterministicMethod
from RandomMethod import RandomMethod
from TrailCalculator import TrailCalculator
from ChartController import ChartController


class ProgramController:

    @staticmethod
    def startAlgorithm(method, dataCollection, iteretionsNumber):
        citiesList = Loader.loadFile(dataCollection)
        trailsLengths = []
        if iteretionsNumber == "N":
            iteretionsNumber = len(citiesList)

        if method == "Metoda losowa":
            for i in range(int(iteretionsNumber)):
                trail = RandomMethod.runRandomMethod(citiesList)
                trailsLengths.append(TrailCalculator.getTrailLength(trail))

        if method == "Metoda zachłanna":
            for i in range(int(iteretionsNumber)):
                trail = DeterministicMethod.runDeterministicMethod(citiesList, i)
                trailsLengths.append(TrailCalculator.getTrailLength(trail))

        ChartController.generateChart(trailsLengths)

        if len(trailsLengths) == 1:
            return round(trailsLengths[0], 2), round(trailsLengths[0], 2), round(trailsLengths[0], 2), round(
                trailsLengths[0], 2)
        else:
            bestSolution = TrailCalculator.getBestSolution(trailsLengths)
            worstSolution = TrailCalculator.getWorstSolution(trailsLengths)
            avg = TrailCalculator.getAvg(trailsLengths)
            sd = TrailCalculator.getSd(trailsLengths)
            return bestSolution, worstSolution, avg, sd
