from creditcard import CreditCardPayment
from paypal import PayPalPayment
from crypto import CryptoPayment
from payment import Payment

# Polimorfizm - rózne obiekty reagują na jedną nazwę matody - pay() -> na różne sposoby!
def process_payment(payment:Payment):
    payment.pay()

payments = [
    CreditCardPayment(760,"678523458524"),
    PayPalPayment(340,"user@gmail.com"),
    CryptoPayment(1900,"0xABCD1234YUJGJL854345")

]

for p in payments:
    process_payment(p)
