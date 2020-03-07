import ProgramController
from tkinter.ttk import *
from tkinter import *


class GuiController:

    def __init__(self):
        # self.programController = ProgramController()
        self.window = Tk()
        self.window.title('SI')
        self.window.configure(background="light blue")
        self.window.geometry("630x500+500+200")
        self.window.resizable(0, 0)

        self.labelTitle = Label(self.window, text="Problem komiwojażera", font="Helvetica 16 bold italic", background="light blue")
        self.labelAlgorithm = Label(self.window, text="Wybierz metodę:", background="light blue")
        self.comboMethods = Combobox(self.window)
        self.comboMethods['values'] = ("Metoda losowa", "Metoda zachłanna", "Algorytm genetyczny")
        self.comboMethods.current(0)
        self.labelIterations = Label(self.window, text="Liczba iteracji:", background="light blue")
        self.labelData = Label(self.window, text="Wybierz zestaw danych:", background="light blue")
        self.entryIterations = Entry(self.window, textvariable=StringVar(self.window, value=1))
        self.comboData = Combobox(self.window)
        self.comboData['values'] = ("ali535", "berlin11", "berlin52")
        self.comboData.current(0)

        self.bestResultText = StringVar()
        self.worstResultText = StringVar()
        self.avgResultText = StringVar()
        self.sdResultText = StringVar()
        self.bestResultText.set("Najlepszy wynik: ")
        self.worstResultText.set("Najgorszy wynik: ")
        self.avgResultText.set("Średnia: ")
        self.sdResultText.set("Odchylenie standardowe: ")

        self.resultsLabel = Label(self.window, text="        Wyniki:          ", font="Helvetica 10 bold italic", background="light blue")
        self.bestResultLabel = Label(self.window, textvariable=self.bestResultText, background="light blue")
        self.worstResultLabel = Label(self.window, textvariable=self.worstResultText, background="light blue")
        self.avgResultLabel = Label(self.window, textvariable=self.avgResultText, background="light blue")
        self.sdResultLabel = Label(self.window, textvariable=self.sdResultText, background="light blue")

        self.labelTitle.grid(columnspan=3, padx=180, pady=20)
        self.labelAlgorithm.grid(column=0, row=1, padx=0, pady=0)
        self.comboMethods.grid(column=1, row=1, padx=0, pady=0)
        self.labelData.grid(column=0, row=3, padx=40)
        self.comboData.grid(column=1, row=3, padx=0, pady=0)
        self.labelIterations.grid(column=0, row=5, padx=40)
        self.entryIterations.grid(column=1, row=5, padx=0, pady=0)
        self.buttonStart = Button(self.window, text="START", bg="green", fg="white", width=10, height=2, font="Helvetica 8 bold",
                                  command=self.startClickListener).grid(column=2,
                                                                        row=2, padx=40)
        self.buttonStop = Button(self.window, text="EXIT", bg="red", fg="white", width=10, height=2, font="Helvetica 8 bold",
                                 command=self.exitClickListener).grid(
            column=2, row=4,
            padx=40)

        self.resultsLabel.grid(column=1, row=6, padx=0, pady=15)
        self.bestResultLabel.grid(column=1, row=7, padx=0, pady=0)
        self.worstResultLabel.grid(column=1, row=8, padx=0, pady=0)
        self.avgResultLabel.grid(column=1, row=9, padx=0, pady=0)
        self.sdResultLabel.grid(column=1, row=10, padx=0, pady=0)
        self.window.mainloop()

    def startClickListener(self):
        enteredMethod = self.comboMethods.get()
        enteredDataCollection = self.comboData.get()
        enteredIteretionsNumber = self.entryIterations.get()

        bestSolution, worstSolution, avg, sd = ProgramController.ProgramController.startAlgorithm(enteredMethod,
                                                                                     enteredDataCollection,
                                                                                     enteredIteretionsNumber)
        self.bestResultText.set("Najlepszy wynik: " + str(bestSolution))
        self.worstResultText.set("Najgorszy wynik: " + str(worstSolution))
        self.avgResultText.set("Średnia: " + str(avg))
        self.sdResultText.set("Odchylenie standardowe: " + str(sd))

    def exitClickListener(self):
        self.window.destroy()
