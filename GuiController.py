import ProgramController
from tkinter.ttk import *
from tkinter import *


class GuiController:

    def __init__(self):
        self.window = Tk()
        self.window.title('SI')
        self.window.configure(background="light blue")
        self.window.geometry("630x550+500+200")
        self.window.resizable(0, 0)

        self.labelTitle = Label(self.window, text="Problem komiwojażera", font="Helvetica 16 bold italic",
                                background="light blue")
        self.labelAlgorithm = Label(self.window, text="Wybierz metodę:", background="light blue")
        self.comboMethods = Combobox(self.window)
        self.comboMethods["values"] = ("Metoda losowa", "Metoda zachłanna", "Algorytm genetyczny")
        self.comboMethods.current(0)
        self.labelIterations = Label(self.window, text="Liczba iteracji:", background="light blue")
        self.labelData = Label(self.window, text="Wybierz zestaw danych:", background="light blue")
        self.iterations = StringVar()
        self.iterations.set("1")
        self.entryIterations = Entry(self.window, textvariable=self.iterations)
        self.comboData = Combobox(self.window)
        self.comboData["values"] = ("ali535", "berlin11", "berlin52")
        self.comboData.current(0)

        self.defaultSettingsLabel = Label(self.window,
                                          text="Gotowe ustawienia testowe (zgodne z instrukcja ćwiczenia):",
                                          background="light blue").grid(column=1, row=6, pady=20)
        self.defaultSettings = IntVar()
        self.radioBtn0 = Radiobutton(self.window, text="Własne ustawienia", variable=self.defaultSettings,
                                     value=0, command=self.checkRadio)
        self.radioBtn1 = Radiobutton(self.window, text="10 000-krotne dla metody losowej",
                                     variable=self.defaultSettings,
                                     value=1, command=self.checkRadio)
        self.radioBtn2 = Radiobutton(self.window, text="N-krotne dla metody zachłannej(N=l.miast)",
                                     variable=self.defaultSettings, value=2, command=self.checkRadio)
        self.radioBtn3 = Radiobutton(self.window, text="10-krotne dla algorytmu ewolucyjnego",
                                     variable=self.defaultSettings,
                                     value=3, command=self.checkRadio)
        self.bestResultText = StringVar()
        self.worstResultText = StringVar()
        self.avgResultText = StringVar()
        self.sdResultText = StringVar()
        self.bestResultText.set("Najlepszy wynik: ")
        self.worstResultText.set("Najgorszy wynik: ")
        self.avgResultText.set("Średnia: ")
        self.sdResultText.set("Odchylenie standardowe: ")
        self.bestResultLabel = Label(self.window, textvariable=self.bestResultText, background="light blue")
        self.worstResultLabel = Label(self.window, textvariable=self.worstResultText, background="light blue")
        self.avgResultLabel = Label(self.window, textvariable=self.avgResultText, background="light blue")
        self.sdResultLabel = Label(self.window, textvariable=self.sdResultText, background="light blue")
        self.resultsLabel = Label(self.window, text="        Wyniki:          ", font="Helvetica 10 bold italic",
                                  background="light blue")

        self.labelTitle.grid(columnspan=3, row=0, padx=180, pady=20)
        self.labelAlgorithm.grid(column=0, row=1, padx=0, pady=0)
        self.comboMethods.grid(column=1, row=1, padx=0, pady=0)
        self.labelData.grid(column=0, row=3, padx=10)
        self.comboData.grid(column=1, row=3, padx=0, pady=0)
        self.labelIterations.grid(column=0, row=5, padx=40)
        self.entryIterations.grid(column=1, row=5, padx=0, pady=0)
        self.buttonStart = Button(self.window, text="START", bg="green", fg="white", width=10, height=2,
                                  font="Helvetica 8 bold",
                                  command=self.startClickListener).grid(column=2,
                                                                        row=2, padx=40)
        self.buttonStop = Button(self.window, text="EXIT", bg="red", fg="white", width=10, height=2,
                                 font="Helvetica 8 bold",
                                 command=self.exitClickListener).grid(
            column=2, row=4,
            padx=40)

        self.radioBtn0.grid(column=1, row=7, padx=10, pady=5)
        self.radioBtn1.grid(column=1, row=8, padx=10, pady=5)
        self.radioBtn2.grid(column=1, row=9, padx=10, pady=5)
        self.radioBtn3.grid(column=1, row=10, padx=10, pady=5)
        self.resultsLabel.grid(column=1, row=11, padx=0, pady=15)
        self.bestResultLabel.grid(column=1, row=12, padx=0, pady=0)
        self.worstResultLabel.grid(column=1, row=13, padx=0, pady=0)
        self.avgResultLabel.grid(column=1, row=14, padx=0, pady=0)
        self.sdResultLabel.grid(column=1, row=15, padx=0, pady=0)
        self.window.mainloop()

    def checkRadio(self):
        if self.defaultSettings.get() == 0:
            self.comboMethods.configure(state='normal')
            self.entryIterations.configure(state='normal')
        elif self.defaultSettings.get() == 1:
            self.comboMethods.current(0)
            self.iterations.set("10000")
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')
        elif self.defaultSettings.get() == 2:
            self.comboMethods.current(1)
            self.iterations.set("N")
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')
        elif self.defaultSettings.get() == 3:
            self.comboMethods.current(2)
            self.iterations.set("10")
            self.comboMethods.configure(state='disabled')
            self.entryIterations.configure(state='disabled')

    def startClickListener(self):
        enteredMethod = self.comboMethods.get()
        enteredDataCollection = self.comboData.get()
        enteredIteretionsNumber = self.entryIterations.get()

        if self.isValidInput(enteredIteretionsNumber):
            bestSolution, worstSolution, avg, sd = ProgramController.ProgramController.startAlgorithm(enteredMethod,
                                                                                                      enteredDataCollection,
                                                                                                      enteredIteretionsNumber)
            self.bestResultText.set("Najlepszy wynik: " + str(bestSolution))
            self.worstResultText.set("Najgorszy wynik: " + str(worstSolution))
            self.avgResultText.set("Średnia: " + str(avg))
            self.sdResultText.set("Odchylenie standardowe: " + str(sd))
        else:
            self.iterations.set("Błędna wartość")

    def isValidInput(self, enteredIteretionsNumber):
        print(isinstance(enteredIteretionsNumber, int))
        if (enteredIteretionsNumber.isdigit() and int(enteredIteretionsNumber) >= 1) or (enteredIteretionsNumber == "N"):
            print(enteredIteretionsNumber)
            return True
        else:
            print(enteredIteretionsNumber)
            return False

    def exitClickListener(self):
        self.window.destroy()
