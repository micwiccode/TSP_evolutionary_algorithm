from Loader import Loader
from DeterministicMethod import DeterministicMethod
from RandomMethod import RandomMethod
from Trail import Trail
from GuiController import GuiController


class Main:

    @staticmethod
    def start():

        GuiController()

        # citiesList = Loader.loadFile('ali535')
        # print(citiesList)
        # trail = RandomMethod.runRandomMethod(citiesList)
        # print(trail)
        # print(Trail.getTrailLength(trail))
        #
        # trail2 = DeterministicMethod.runDeterministicMethod(citiesList)
        # print(trail2)
        # print(Trail.getTrailLength(trail2))




