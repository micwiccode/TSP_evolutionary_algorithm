from CrossOver import CrossOver
from random import randrange


class CXCrossOver(CrossOver):
    def __init__(self, firstParent, secondParent):
        super().__init__(firstParent, secondParent)

    def cross(self):

        beginingPointIndex = randrange(len(self.firstParent))
        beginingPoint = self.firstParent[beginingPointIndex]
        firstParentIndexes = [beginingPointIndex]

        secondPoint = -1
        firstPointIndex = beginingPointIndex
        while secondPoint != beginingPoint:
            secondPoint = self.secondParent[firstPointIndex]
            for i in range(len(self.firstParent)):
                if self.firstParent[i] == secondPoint:
                    firstPointIndex = i
                    firstParentIndexes.append(i)

        child = []
        for i in range(len(self.firstParent)):
            if i in firstParentIndexes:
                child.append(self.firstParent[i])
            else:
                child.append(self.secondParent[i])
        return child
