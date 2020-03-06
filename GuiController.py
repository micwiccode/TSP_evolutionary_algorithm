from tkinter.ttk import *
from tkinter import *


class GuiController():

    def __init__(self):
        print("init")
        window = Tk()
        window.title('SI')
        window.configure(background="snow")
        window.geometry("600x500+500+200")
        window.resizable(0, 0)

        labelTitle = Label(window, text="Problem komiwojażera", font = "Helvetica 16 bold italic")
        labelTitle.grid(columnspan=3, padx=180, pady=20)

        labelAlgorithm = Label(window, text="Wybierz metodę:")
        labelAlgorithm.grid(column=0, row=1, padx=0, pady=0)
        combo1 = Combobox(window)
        combo1['values'] = ("Metoda losowa", "Metoda zachłanna", "Algorytm genetyczny")
        combo1.current(1)
        combo1.grid(column=1, row=1, padx=0, pady=0)

        labelIterations = Label(window, text="Liczba iteracji:")
        labelData = Label(window, text="Wybiezr zestaw danych:")
        entryIterations = Entry(window)

        combo2 = Combobox(window)
        combo2['values'] = ("ali535", "berlin11", "berlin52")
        combo2.current(1)

        labelData.grid(column=0, row=3, padx=40)
        combo2.grid(column=1, row=3, padx=0, pady=0)
        labelIterations.grid(column=0, row=5, padx=40)
        entryIterations.grid(column=1, row=5, padx=0, pady=0)

        buttonStart = Button(window, text="START", bg="green", fg="white", width=10, height=2).grid(column=2, row=2, padx=40)
        buttonStop = Button(window, text="STOP", bg="red", fg="white", width=10, height=2).grid(column=2, row=4, padx=40)

        # self.textentry = Entry(window, width=20, bg="white").grid(row=2, column=0, sticky=W)

        window.mainloop()

    def click(self):
        entered_iteretions_number = self.textentry.get()
        print(entered_iteretions_number)
