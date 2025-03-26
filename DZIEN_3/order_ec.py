class Order:
    tax_rate = 0.23 #podatek VAT 23%

    def __init__(self,product_name,unit_price,quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    #metoda instancyjna - operuje na danych konkretnego zamówienia
    def total_price_with_tax(self):
        total = self.unit_price*self.quantity
        return total*(1+Order.tax_rate)

    #metoda statyczna
    @staticmethod
    def convert_currency(amount,rate):
        return amount*rate


#tworzymy zamówienie
order = Order("Laptop XY",4560,2)

#koszt całkowity z podatkiem
total = order.total_price_with_tax()
print(f"Kwota całkowita z VAT: {total:.2f} zł")

#przeliczamy na EURO(przyjmijmy że 1EUR = 4.5 zł)
total_eur = Order.convert_currency(total,1/4.5)
print(f"Kwota całkowita z VAT w EUR: {total_eur:.2f}")
