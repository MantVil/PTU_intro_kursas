from tkinter import *

langas = Tk()

def spaudinti_su_enter():
    print("spausdina paspaudus ENTER....")
def spaudinti_su_kairiu(event):
    print("spausdina paspaudus Kairi....")
def spaudinti_su_desiniu(event):
    print("spausdina paspaudus Desini....")

mygtukas = Button(langas, text="spausdinti")
mygtukas.bind("<Button-1>", spaudinti_su_kairiu)
mygtukas.bind("<Button-3>", spaudinti_su_desiniu)
langas.bind("<Return>", lambda event: spaudinti_su_enter())
mygtukas.pack()
langas.mainloop()
