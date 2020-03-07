class Loader:

    def loadFile(file):
        dataFile = open('TSP/' + file + '.tsp', 'r')
        name = dataFile.readline().strip().split()[1]  # NAME
        fileType = dataFile.readline().strip().split()[1]  # TYPE
        comment = dataFile.readline().strip().split()[1]  # COMMENT
        dimension = dataFile.readline().strip().split()[1]  # DIMENSION
        edgeWeightType = dataFile.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
        dataFile.readline()

        # Read nodes
        citiesList = []
        for i in range(0, int(dimension)):
            x, y = dataFile.readline().strip().split()[1:]
            citiesList.append([float(x), float(y)])

        # Close input file
        dataFile.close()
        return citiesList
