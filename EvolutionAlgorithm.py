import random

from RandomAlgorithm import RandomAlgorithm
from Algorithm import Algorithm
from OXCrossOver import OXCrossOver
from CXCrossOver import CXCrossOver
from SwapMutation import SwapMutation
from InversionMutation import InversionMutation
from random import sample, randrange, uniform


class EvolutionAlgorithm(Algorithm):

    def __init__(self, citiesList, numberOfGenerations, edgeWeightType, popSize, propCross, propMutate, tourSize, mutationType, crossType):
        super().__init__(citiesList, numberOfGenerations, edgeWeightType)
        self.currentPopulation = []
        self.nextPopulation = []
        self.selectedIndividuals = None
        self.popSize = popSize
        self.crossProp = propCross
        self.mutateProp = propMutate
        self.tourSize = tourSize
        self.crossType = crossType
        self.mutationType = mutationType
        self.selectionType = 'TOUR'
        self.bests = []
        self.avarages = []
        self.worsts = []
        self.sds = []

    def start(self):
        super().start()
        self.initialisePopulation()
        for i in range(self.numberOfGenerations):
            self.evaluatePopulation()
            while len(self.nextPopulation) != self.popSize:
                firstParent = self.selectIndividual()
                secondParent = self.selectIndividual()
                if random.uniform(0, 1) < self.crossProp:
                    newIndividual = self.crossOverIndividuals(firstParent, secondParent)
                else:
                    newIndividual = firstParent
                if random.uniform(0, 1) < self.mutateProp:
                    newIndividual = self.mutateIndividual(newIndividual)
                self.nextPopulation.append(newIndividual)
            self.currentPopulation = self.nextPopulation
            self.nextPopulation = []
        return self.bests, self.avarages, self.worsts, self.sds

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

    def selectIndividual(self):
        bestIndividual = None
        if self.selectionType == 'TOUR':
            individuals = sample(self.currentPopulation, self.tourSize)
            bestIndividualFitness = float("inf")
            for i in range(self.tourSize):
                currentIndividualFitness = self.getTrailLength(individuals[i])
                if currentIndividualFitness < bestIndividualFitness:
                    bestIndividual = individuals[i]
                    bestIndividualFitness = currentIndividualFitness
        return bestIndividual

    def crossOverIndividuals(self, firstParent, secondParent):
        global child
        if self.crossType == 'OX':
            oxCrossOver = OXCrossOver(firstParent, secondParent)
            child = oxCrossOver.cross()
        if self.crossType == 'CX':
            cxCrossOver = CXCrossOver(firstParent, secondParent)
            child = cxCrossOver.cross()
        return child

    def mutateIndividual(self, individual):
        if self.mutationType == 'SWAP':
            swap = SwapMutation(individual)
            individual = swap.mutate()

        if self.mutationType == 'INVERSION':
            inversion = InversionMutation(individual)
            individual = inversion.mutate()

        return individual
