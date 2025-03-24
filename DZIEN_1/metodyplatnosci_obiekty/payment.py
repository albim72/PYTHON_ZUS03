from abc import ABC,abstractmethod

# Abstrakcja - definiujemy klasę abstrakcyjną - dziedziczenie ABC
class Payment(ABC):
    def __init__(self,amount):
        self.__amount = amount # enkapsulacja - prywatny atrybut
        
    @abstractmethod
    def pay(self):
        pass
    
    
    #dostęp do prywatnego pola przez metodę
    def get_amount(self):
        return self.__amount
    
    def set_amount(self,newamount):
        self.__amount = newamount
