class Samochod:
    #opis stanu - konstruktor
    def __init__(self,marka,kolor):
        self.marka = marka
        self.kolor = kolor
        #lewa strona - zmienna po kontekście, prawa strona - atrybut konstruktora init

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Samochod)

    def __repr__(self):
        return f"Nowy obiekt klasy {self.__class__.__name__} -> {self.marka}"

    #zachowanie obiektu - metody
    def jedz(self):
        print(f"{self.marka} jedzie!")

    def info(self):
        print(f"Samochód marki {self.marka} jest koloru {self.kolor}.")
