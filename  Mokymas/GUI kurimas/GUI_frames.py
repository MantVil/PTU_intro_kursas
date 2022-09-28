from tkinter import Y, Tk, Frame, Button, BOTTOM, LEFT, Y
langas = Tk()
langas.geometry("400x300")
virsus = Frame(langas)
apatinis = Frame(langas)
# mygtukai freimuose
mygtukas1 = Button(virsus, text="Pirmas")
mygtukas2 = Button(virsus, text="Antras")
mygtukas3 = Button(virsus, text="Trecias")
mygtukas4=Button(apatinis, text="Paskutinis")

# pakuojam
virsus.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)
# paleidimas
langas.mainloop()