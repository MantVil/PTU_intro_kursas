# Faile kursas.py sukurti objekto klasę Kursas, kuri turėtų savybes pavadinimas, destytojas, trukme, taip pat metodą destyti(), kuris spausdintų „Vyksta mokymas!“

class Kursas:
    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme
    
    def destyti(self):
        print("Vyksta destymas")
        