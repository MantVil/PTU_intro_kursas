from tkinter import Label, Tk, LabelFrame

langas = Tk()
langas.geometry("500x300")
uzrasas = Label(langas, text="Sveiki, studentai!")
uzrasas2 = Label(langas, text="Sveiki, antradieni!")
uzrasas.pack()
uzrasas2.pack(side='bottom')
langas.mainloop()