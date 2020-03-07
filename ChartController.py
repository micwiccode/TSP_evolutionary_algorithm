import matplotlib.pyplot as plt


class ChartController:

    def generateChart(trailsLengths):
        if len(trailsLengths) == 1:
            plt.scatter(1, trailsLengths)
            plt.ion()
            plt.show()
        else:
            plt.plot(trailsLengths)
            plt.ylabel('Distance')
            plt.xlabel('Number of iteretions')
            plt.ion()
            plt.show()
