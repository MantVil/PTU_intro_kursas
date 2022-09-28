from tkinter import *
import webbrowser

langas = Tk()
langas.geometry("300x100")

meniukas = Menu(langas)
langas.config(menu=meniukas)
submeniukas = Menu(meniukas, tearoff=0)
submeniukas2 = Menu(meniukas, tearoff=0)
submeniukas3 = Menu(meniukas, tearoff=0)



def pirmas():
    label_pasirinkta["text"] = "Pirmas"

def antras():
    label_pasirinkta["text"] = "Antras!"

def trecias():
    label_pasirinkta["text"] = "Paskutinis is triju!"

def tell_a_joke():
    label_pasirinkta["text"] = "You are not funny! HAHA"

def fart():
    label_pasirinkta["text"] = "pirst"

def callback(url):
    webbrowser.open_new(url)

def launch_url(event):
    url = entry_url.get()
    callback(url)
    label_pasirinkta["text"] = f"Paleidom browseri su {url}"

meniukas.add_cascade(label="Meniukas", menu=submeniukas)
submeniukas.add_command(label="Pirmas", command=pirmas)
submeniukas.add_command(label="Antras", command=antras)
submeniukas.add_separator()
submeniukas.add_command(label="Trecias", command=trecias)

meniukas.add_cascade(label="Fun", menu=submeniukas2)
submeniukas2.add_command(label="tell a joke", command=tell_a_joke)
submeniukas2.add_command(label="Fart!", command=fart)

meniukas.add_cascade(label="Settings", menu= submeniukas3)
submeniukas3.add_radiobutton(label= "setting 1")
submeniukas3.add_radiobutton(label="Setting 2")

label_iveskite_adresa = Label(langas, text="Enter URL:")
entry_url = Entry(langas)
langas.bind("<Return>", launch_url)

label_pasirinkta = Label(langas, text="....Kolkas nieko...", bd =3, relief=SUNKEN, anchor = W)
label_pasirinkta.pack(side=BOTTOM, fill=X)

label_iveskite_adresa.pack(side=TOP)
entry_url.pack(side=TOP)


langas.mainloop()

