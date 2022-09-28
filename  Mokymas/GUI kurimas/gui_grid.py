from tkinter import *

langas = Tk()
l_vardas = Label(langas, text="Vardas")
e_vardas = Entry(langas)
l_pavarde = Label(langas, text="Pavarde")
e_pavarde = Entry(langas)

l_vardas.grid(row=0, column=0, sticky=W)
e_vardas.grid(row=0,column=1)
l_pavarde.grid(row=1,column=0, sticky=E)
e_pavarde.grid(row=1,column=1)

langas.mainloop()
