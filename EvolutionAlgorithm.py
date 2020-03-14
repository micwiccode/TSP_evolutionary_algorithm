import random

from RandomAlgorithm import RandomAlgorithm
from Algorithm import Algorithm
from random import sample, randrange


class EvolutionAlgorithm(Algorithm):

    def __init__(self, citiesList, numberOfGenerations, edgeWeightType):
        super().__init__(citiesList, numberOfGenerations, edgeWeightType)
        self.currentPopulation = []
        self.nextPopulation = []
        self.selectedIndividuals = None
        self.popSize = 10
        self.crossProp = 0.7
        self.mutateProp = 0.1
        self.tourSize = 5
        self.crossType = 'OX'
        self.mutationType = 'SWAP'
        self.selectionType = 'TOUR'
        self.bests = []
        self.avarages = []
        self.worsts = []
        self.sds = []

    def start(self):
        super().start()
        self.initialisePopulation()

        for i in range(int(self.numberOfGenerations)):
            self.evaluatePopulation()
            while len(self.nextPopulation) != self.popSize:
                firstParent = self.selectIndividual()
                secondParent = self.selectIndividual()

                if random.uniform(0, 1) > self.crossProp:
                    newIndividual = self.crossOverIndividuals(firstParent, secondParent)
                else:
                    newIndividual = firstParent
                if random.uniform(0, 1) > self.mutateProp:
                    newIndividual = self.mutateIndividual(newIndividual)

                self.nextPopulation.append(newIndividual)

            self.currentPopulation = self.nextPopulation

        return self.bests, self.avarages, self.worsts, self.sds

    # def runEvolutionMethod(self, startCityIndex):
    #     self.initialisecurrentPopulation()
    #     numberOfCities = len(self.citiesList)
    #     currentCityIndex = startCityIndex
    #     visitedCitiesIndexes = [startCityIndex]
    #     trail = [self.citiesList[startCityIndex]]

    def initialisePopulation(self):
        randomAlgorithm = RandomAlgorithm(self.citiesList, self.numberOfGenerations, self.edgeWeightType)
        for i in range(self.popSize):
            individual = randomAlgorithm.runRandomMethod()
            self.currentPopulation.append(individual)

    def evaluatePopulation(self):
        trailsLengths = []
        for i in range(self.popSize):
            trailsLengths.append(self.getTrailLength(self.currentPopulation[i]))
        _, bestSolution, worstSolution, avg, sd = self.resultsAnalyzer.analiseResult(trailsLengths)
        self.bests.append(bestSolution)
        self.avarages.append(worstSolution)
        self.worsts.append(avg)
        self.sds.append(sd)

    # def evaluateIndividual(self):
    #     trailsLengths = []
    #     for i in range(self.popSize):
    #         trailsLengths[i] = self.getTrailLength(self.currentPopulation[i])
    #     bestSolution, worstSolution, avg, _ = self.resultsAnalyzer.analiseResult(trailsLengths)
    #     self.bests.append(bestSolution)
    #     self.avarages.append(worstSolution)
    #     self.worsts.append(avg)

    def selectIndividual(self):
        bestIndividual = None
        if self.selectionType == 'TOUR':
            individuals = sample(self.currentPopulation, self.tourSize)
            bestIndividualFitness = 0
            for i in range(self.tourSize):
                currentIndividualFitness = self.getTrailLength(individuals[i])
                if currentIndividualFitness > bestIndividualFitness:
                    bestIndividual = individuals[i]
        return bestIndividual

    def crossOverIndividuals(self, firstParent, secondParent):
        global child
        if self.crossType == 'OX':
            firstCut = randrange(len(firstParent))
            secondCut = randrange(len(firstParent))
            while firstCut == secondCut:
                secondCut = randrange(len(firstParent))

            if firstCut > secondCut:
                temp = firstCut
                firstCut = secondCut
                secondCut = temp

            firstParentCandidates = []
            secondParentCandidates = []
            child = []

            for i in range(len(firstParent)):
                if (firstCut <= i) and (i < secondCut):
                    child.append(firstParent[i])
                    firstParentCandidates.append(firstParent[i])
                else:
                    child.append(None)

            for i in range(len(secondParent)):
                if not (secondParent[i] in firstParentCandidates):
                    secondParentCandidates.append(secondParent[i])

            index = 0
            for i in range(len(firstParent)):
                if child[i] is None:
                    child[i] = secondParentCandidates[index]
                    index += 1
        return child

    def mutateIndividual(self, individual):
        if self.mutationType == 'SWAP':
            firstPosition = randrange(len(individual))
            secondPosition = randrange(len(individual))

            while firstPosition == secondPosition:
                secondPosition = randrange(len(individual))

            individual[firstPosition], individual[secondPosition] = individual[secondPosition], individual[firstPosition]
            return individual
