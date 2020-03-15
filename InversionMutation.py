from Mutation import Mutation
from random import randrange


class InversionMutation(Mutation):
    def __init__(self, individual):
        super().__init__(individual)

    def mutate(self):
        firstPosition = randrange(len(self.individual))
        secondPosition = randrange(len(self.individual))

        while firstPosition == secondPosition:
            secondPosition = randrange(len(self.individual))

        if firstPosition > secondPosition:
            temp = firstPosition
            firstPosition = secondPosition
            secondPosition = temp

        while firstPosition < secondPosition:
            temp = self.individual[firstPosition]
            self.individual[firstPosition] = self.individual[secondPosition]
            self.individual[secondPosition] = temp
            firstPosition += 1
            secondPosition -= 1

        return self.individual
