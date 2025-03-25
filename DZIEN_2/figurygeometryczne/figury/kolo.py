from figura import Figura
import math

#stwórz klasę Kolo(Figura) - zbuduj konstrukor dla tej klasy w oparciu o klasę Figura
#zaimplementuj metodę policz_pole() -> pi*r**2
#w main stówrz obiekt klasy Kolo i policz jego pole

class Kolo(Figura):
    def __init__(self,a):
        super().__init__(a)

    def policz_pole(self):
        return math.pi*self.a**2




