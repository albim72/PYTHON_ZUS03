from payment import Payment

# Dziedziczenie - różne klasy płatności otrzymują definicję po klasie Payment!
class CreditCardPayment(Payment):
    def __init__(self,amount,card_number):
        super().__init__(amount)
        self.__card_number = card_number

    def pay(self):
        print(f"Płatnośc {self.get_amount()} zł z użyciem karty kredytowej kończącej się na "
              f"{str(self.__card_number)[-4:]}")
