from payment import Payment

class PayPalPayment(Payment):
    def __init__(self,amount,email):
        super().__init__(amount)
        self.__email = email

    def pay(self):
        print(f"Płatnośc {self.get_amount()} zł z użyciem konta PayPal "
              f"{self.__email}")
