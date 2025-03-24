class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance  #atrybut chroniony

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("Saldo nie może byc ujemne!")
        self._balance = value

    #property tylko do odczytu
    @property
    def is_rich(self):
        return self._balance > 1_000_000


konto = BankAccount("Jan Kowalski",50000)
print(f"Aktualne saldo: {konto.balance} zł")
konto.balance += 12300
print(f"Nowe saldo: {konto.balance} zł")
print(f"Czy właściciel ma status VIP? {konto.is_rich}")

try:
    konto.balance = -9000
except ValueError as ve:
    print(f"błąd: {ve}")



