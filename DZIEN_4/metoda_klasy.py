class Pracownik:
    def __init__(self,imie,nazwisko,pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def info(self):
        return f"{self.imie} {self.nazwisko} zarabia {self.pensja} PLN"

    @classmethod
    def from_string(cls,tekst):
        """Tworzy obiekt klasy Pracownik na podstawie tekstu"""
        imie,nazwisko,pensja = tekst.split()
        return cls(imie.strip(),nazwisko.strip(),int(pensja.strip()))

#utworzenie obiektu staandardowo
p1 = Pracownik("Anna","Król",5600)

#utworzenie obiektu z tekstu
p2 = Pracownik.from_string("Jan, Nowak, 6700")

print(p1.info())
print(type(p1))

print(p2.info())
print(type(p2))


