from Mutation import Mutation
from random import randrange


class SwapMutation(Mutation):
    def __init__(self, individual):
        super().__init__(individual)

    def mutate(self):
        firstPosition = randrange(len(self.individual))
        secondPosition = randrange(len(self.individual))

        while firstPosition == secondPosition:
            secondPosition = randrange(len(self.individual))

        temp = self.individual[firstPosition]
        self.individual[firstPosition] = self.individual[secondPosition]
        self.individual[secondPosition] = temp

        return self.individual
