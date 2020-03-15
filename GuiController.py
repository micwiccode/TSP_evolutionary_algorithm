from AlgorithmController import AlgorithmController
from tkinter.ttk import *
from tkinter import *


class GuiController:

    def __init__(self):
        self.window = Tk()
        self.window.title('SI')
        self.window.configure(background='light blue')
        self.window.geometry('650x750+500+50')
        self.window.resizable(0, 0)

        self.labelTitle = None
        self.labelAlgorithm = None
        self.comboMethods = None
        self.labelIterations = None
        self.labelData = None
        self.entryIterations = None
        self.comboData = None
        self.iterations = None
        self.buttonStart = None
        self.buttonStop = None

        self.evolutionAlgorithmLabel = None
        self.popSizeLabel = None
        self.genLabel = None
        self.pxLabel = None
        self.pmLabel = None
        self.tourLabel = None
        self.popSizeEntry = None
        self.genEntry = None
        self.pxEntry = None
        self.pmEntry = None
        self.tourEntry = None

        self.defaultSettingsLabel = None
        self.defaultSettings = None
        self.radioBtn0 = None
        self.radioBtn1 = None
        self.radioBtn2 = None
        self.radioBtn3 = None

        self.bestResultLabel = None
        self.worstResultLabel = None
        self.avgResultLabel = None
        self.sdResultLabel = None
        self.timeResultLabel = None
        self.resultsLabel = None

        self.defaultSettings = IntVar()
        self.iterations = StringVar()
        self.bestResultText = StringVar()
        self.worstResultText = StringVar()
        self.avgResultText = StringVar()
        self.sdResultText = StringVar()
        self.timeResultText = StringVar()
        self.popSize = IntVar()
        self.px = IntVar()
        self.pm = IntVar()
        self.tourSize = IntVar()
        self.iterations.set('1')
        self.popSize.set(10)
        self.px.set(0.7)
        self.pm.set(0.1)
        self.tourSize.set(5)
        self.bestResultText.set('Najlepszy wynik: ')
        self.worstResultText.set('Najgorszy wynik: ')
        self.avgResultText.set('Średnia: ')
        self.sdResultText.set('Odchylenie standardowe: ')
        self.timeResultText.set('Czas: ')

        self.renderMainElements(self.window)
        self.renderEAElements(self.window)
        self.renderDefaultOptionsElements(self.window)
        self.renderResultsElements(self.window)

        self.window.mainloop()

    def renderMainElements(self, window):
        self.labelTitle = Label(window, text='Problem komiwojażera', font='Helvetica 16 bold italic',
                                background='light blue')
        self.labelAlgorithm = Label(window, text='Wybierz metodę:', background='light blue')
        self.comboMethods = Combobox(window)
        self.comboMethods['values'] = ('Metoda losowa', 'Metoda zachłanna', 'Algorytm ewolucyjny')
        self.comboMethods.current(0)
        self.labelIterations = Label(window, text='Liczba pokoleń:', background='light blue')
        self.labelData = Label(window, text='Wybierz zestaw danych:', background='light blue')
        self.entryIterations = Entry(window, textvariable=self.iterations)
        self.comboData = Combobox(window)
        self.comboData['values'] = (
            'ali535', 'berlin11', 'berlin52', 'fl417', 'gr666', 'kroA100', 'kroA150', 'kroA200', 'nrw1379', 'pr2392')
        self.comboData.current(0)
        self.buttonStart = Button(window, text='START', bg='green', fg='white', width=10, height=2,
                                  font='Helvetica 8 bold',
                                  command=self.startClickListener)
        self.buttonStop = Button(window, text='EXIT', bg='red', fg='white', width=10, height=2,
                                 font='Helvetica 8 bold',
                                 command=self.exitClickListener)

        self.labelTitle.grid(columnspan=3, row=0, padx=180, pady=20)
        self.labelAlgorithm.grid(column=0, row=1)
        self.comboMethods.grid(column=1, row=1)
        self.labelData.grid(column=0, row=3, padx=10)
        self.comboData.grid(column=1, row=3)
        self.labelIterations.grid(column=0, row=5, padx=40)
        self.entryIterations.grid(column=1, row=5)
        self.buttonStart.grid(column=2, row=2, padx=40)
        self.buttonStop.grid(column=2, row=4, padx=40)

    def renderEAElements(self, window):
        self.evolutionAlgorithmLabel = Label(window,
                                             text='Parametry algorytmu ewolucyjnego:',
                                             background='light blue')
        self.popSizeLabel = Label(window,
                                  text='Rozmiar populacji:',
                                  background='light blue')
        self.pxLabel = Label(window,
                             text='Prawd. krzyżowania:',
                             background='light blue')
        self.pmLabel = Label(window,
                             text='Prawd. mutacji:',
                             background='light blue')
        self.tourLabel = Label(window,
                               text='Rozmiar turnieju:',
                               background='light blue')

        self.evolutionAlgorithmLabel.grid(column=1, row=6, pady=20)
        self.popSizeLabel.grid(column=0, row=7)
        self.pxLabel.grid(column=0, row=9)
        self.pmLabel.grid(column=0, row=10)
        self.tourLabel.grid(column=0, row=11)

        self.popSizeEntry = Entry(window, textvariable=self.popSize)
        self.pxEntry = Entry(window, textvariable=self.px)
        self.pmEntry = Entry(window, textvariable=self.pm)
        self.tourEntry = Entry(window, textvariable=self.tourSize)

        self.popSizeEntry.grid(column=1, row=7)
        self.pxEntry.grid(column=1, row=9)
        self.pmEntry.grid(column=1, row=10)
        self.tourEntry.grid(column=1, row=11)

    def renderDefaultOptionsElements(self, window):
        self.defaultSettingsLabel = Label(window,
                                          text='Gotowe ustawienia testowe (zgodne z instrukcja ćwiczenia):',
                                          background='light blue').grid(column=1, row=12, pady=20)
        self.radioBtn0 = Radiobutton(window, text='Własne ustawienia', variable=self.defaultSettings,
                                     value=0, command=self.checkRadio).grid(column=1, row=13, padx=10, pady=5)
        self.radioBtn1 = Radiobutton(window, text='10 000-krotne dla metody losowej',
                                     variable=self.defaultSettings,
                                     value=1, command=self.checkRadio).grid(column=1, row=14, padx=10, pady=5)
        self.radioBtn2 = Radiobutton(window, text='N-krotne dla metody zachłannej(N=l.miast)',
                                     variable=self.defaultSettings, value=2, command=self.checkRadio).grid(column=1,
                                                                                                           row=15,
                                                                                                           padx=10,
                                                                                                           pady=5)
        self.radioBtn3 = Radiobutton(window, text='10-krotne dla algorytmu ewolucyjnego',
                                     variable=self.defaultSettings,
                                     value=3, command=self.checkRadio).grid(column=1, row=16, padx=10, pady=5)

    def renderResultsElements(self, window):
        self.bestResultLabel = Label(window, textvariable=self.bestResultText, background='light blue')
        self.worstResultLabel = Label(window, textvariable=self.worstResultText, background='light blue')
        self.avgResultLabel = Label(window, textvariable=self.avgResultText, background='light blue')
        self.sdResultLabel = Label(window, textvariable=self.sdResultText, background='light blue')
        self.timeResultLabel = Label(window, textvariable=self.timeResultText, background='light blue')
        self.resultsLabel = Label(window, text='        Wyniki:          ', font='Helvetica 10 bold italic',
                                  background='light blue')
        self.resultsLabel.grid(column=1, row=17, pady=15)
        self.bestResultLabel.grid(column=1, row=18)
        self.worstResultLabel.grid(column=1, row=19)
        self.avgResultLabel.grid(column=1, row=20)
        self.sdResultLabel.grid(column=1, row=21)
        self.timeResultLabel.grid(column=1, row=22)

    def checkRadio(self):
        if self.defaultSettings.get() == 0:
            self.comboMethods.configure(state='normal')
            self.entryIterations.configure(state='normal')
        elif self.defaultSettings.get() == 1:
            self.comboMethods.current(0)
            self.iterations.set('10000')
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')
        elif self.defaultSettings.get() == 2:
            self.comboMethods.current(1)
            self.iterations.set('N')
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')
        elif self.defaultSettings.get() == 3:
            self.comboMethods.current(2)
            self.iterations.set('10')
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')

    def startClickListener(self):
        enteredMethod = self.comboMethods.get()
        enteredDataCollection = self.comboData.get()
        numberOfGenerations = self.entryIterations.get()

        popSize = self.popSizeEntry.get()
        propCross = self.pxEntry.get()
        propMutate = self.pmEntry.get()
        tourSize = self.tourEntry.get()

        if self.isValidGeneralInput(enteredMethod, numberOfGenerations, popSize, propCross, propMutate, tourSize):
            programController = AlgorithmController(enteredMethod, enteredDataCollection)
            bestSolution, worstSolution, avg, sd, time = programController.startAlgorithm(int(numberOfGenerations),
                                                                                          int(popSize),
                                                                                          float(propCross),
                                                                                          float(propMutate),
                                                                                          int(tourSize))
            self.bestResultText.set('Najlepszy wynik: ' + str(bestSolution))
            self.worstResultText.set('Najgorszy wynik: ' + str(worstSolution))
            self.avgResultText.set('Średnia: ' + str(avg))
            self.sdResultText.set('Odchylenie standardowe: ' + str(sd))
            self.timeResultText.set('Czas: ' + str(time) + ' s')

    def isValidGeneralInput(self, enteredMethod, numberOfGenerations, popSize, propCross, propMutate, tourSize):
        if (numberOfGenerations.isdigit() and int(numberOfGenerations) >= 1) or (
                numberOfGenerations == 'N'):
            if enteredMethod == 'Algorytm ewolucyjny':
                if self.isValidEAInputs(popSize, propCross, propMutate, tourSize):
                    return True
                else:
                    return False
            return True
        else:
            self.iterations.set('Błędna wartość')
            return False

    def isValidEAInputs(self, popSize, propCross, propMutate, tourSize):
        print(popSize)
        print(propCross)
        print(propMutate)
        print(tourSize)
        print(popSize.isdigit())
        print(propCross.isdigit())
        print(propMutate.isdigit())
        print(tourSize.isdigit())
        isValid = True
        if not (popSize.isdigit() and int(popSize) >= 1):
            self.popSize.set('Błędna wartość')
            isValid = False
        if not (0 <= float(propCross) <= 1):
            self.px.set('Błędna wartość')
            isValid = False
        if not (0 <= float(propMutate) <= 1):
            self.pm.set('Błędna wartość')
            isValid = False
        if not (tourSize.isdigit() and int(popSize) >= int(tourSize) >= 1):
            self.tourSize.set('Błędna wartość')
            isValid = False
        return isValid

    def exitClickListener(self):
        self.window.destroy()
