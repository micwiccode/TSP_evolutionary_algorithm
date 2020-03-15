from CrossOver import CrossOver
from random import randrange


class OXCrossOver(CrossOver):
    def __init__(self, firstParent, secondParent):
        super().__init__(firstParent, secondParent)

    def cross(self):
        firstCut = randrange(len(self.firstParent))
        secondCut = randrange(len(self.firstParent))
        while firstCut == secondCut:
            secondCut = randrange(len(self.firstParent))

        if firstCut > secondCut:
            temp = firstCut
            firstCut = secondCut
            secondCut = temp

        firstParentCandidates = []
        secondParentCandidates = []
        child = []

        for i in range(len(self.firstParent)):
            if (firstCut <= i) and (i < secondCut):
                child.append(self.firstParent[i])
                firstParentCandidates.append(self.firstParent[i])
            else:
                child.append(None)

        for i in range(len(self.secondParent)):
            if not (self.secondParent[i] in firstParentCandidates):
                secondParentCandidates.append(self.secondParent[i])

        index = 0
        for i in range(len(self.firstParent)):
            if child[i] is None:
                child[i] = secondParentCandidates[index]
                index += 1

        return child
