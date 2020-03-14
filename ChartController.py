import matplotlib.pyplot as plt


class ChartController:

    @staticmethod
    def generateChart(trailsLengths, bestSolutions, worstSolutions, avgs):
        print(bestSolutions)
        print(worstSolutions)
        print(avgs)
        if trailsLengths is None:
            if len(bestSolutions) == 1:
                plt.scatter(1, bestSolutions)
                plt.scatter(1, worstSolutions)
                plt.scatter(1, avgs)
            else:
                print('ok')
                plt.plot(bestSolutions, label='best')
                plt.plot(worstSolutions, label='best')
                plt.plot(avgs, label='best')
        else:
            if len(trailsLengths) == 1:
                plt.scatter(1, trailsLengths)
            else:
                plt.plot(trailsLengths)
        plt.ylabel('Odległość')
        plt.xlabel('Liczba iteracji/pokoleń')
        plt.ion()
        plt.show()
