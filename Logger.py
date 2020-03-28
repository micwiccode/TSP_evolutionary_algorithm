class Logger:
    def __init__(self, method, dataCollection, numberOfGenerations, popSize, propCross, propMutate,
                 tourSize, mutationType, crossType, bestSolution, worstSolution, avg, sd, time):
        self.method = method
        self.dataCollection = dataCollection
        self.numberOfGenerations = numberOfGenerations
        self.popSize = popSize
        self.propCross = propCross
        self.propMutate = propMutate
        self.tourSize = tourSize
        self.mutationType = mutationType
        self.crossType = crossType
        self.bestSolution = bestSolution
        self.worstSolution = worstSolution
        self.avg = avg
        self.sd = sd
        self.time = time
        self.result = ''

    def logResults(self):
        self.result = '\nMetoda: ' + self.method + '\nKolekcja danych: ' + self.dataCollection + '\nLiczba generacji: ' + str(
            self.numberOfGenerations)
        if self.method == 'Algorytm ewolucyjny':
            self.result += '\nParametry alg. genetycznego:\n----------------------------\nRozmiar populacji: ' + str(
                self.popSize) + '\nTyp selekcji: TOUR'
            self.result += '\nRozmiar turnieju: ' + str(
                self.tourSize) + '\nTyp krzyżowania: ' + self.crossType + '\nTyp mutacji: ' + str(self.mutationType)
            self.result += '\nPrawdopodobieństwo krzyżowania: ' + str(
                self.propCross) + '\nPrawdopodobieństwo mutacji: ' + str(self.propMutate)

        self.result += '\nRozwiązania:\n----------------------------\nNajlepsze rozwiązanie: ' + str(self.bestSolution)
        self.result += '\nNajgorsze rozwiązanie: ' + str(self.worstSolution)
        self.result += '\nŚrednia: ' + str(self.avg)
        self.result += '\nOdchylenie standardowe: ' + str(self.sd)
        self.result += '\nCzas: ' + str(self.time)
        print(self.result)

    def saveResultsInFile(self):
        file = open('wyniki.txt', 'w')
        file.write(self.result)
        file.close()
