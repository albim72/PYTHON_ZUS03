from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self,a,b=None):
        self.a=a
        if b:
            self.b=b

    @abstractmethod
    def policz_pole(self):
        pass


