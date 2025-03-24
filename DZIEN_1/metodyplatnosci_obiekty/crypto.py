from payment import Payment

class CryptoPayment(Payment):
    def __init__(self,amount,wallet_address):
        super().__init__(amount)
        self.__wallet_address = wallet_address

    def pay(self):
        print(f"Płatnośc {self.get_amount()} zł z użyciem portfela Crypto "
              f"{self.__wallet_address[:6]}...")
