class CarRepair:
    def __init__(self, car_model):
        self.car_model = car_model
        self._parts_cost = 0
        self._labor_hours = 0
        self.labor_rate = 150  # zł za godzinę robocizny

    @property
    def parts_cost(self):
        """Koszt części zamiennych"""
        return self._parts_cost

    @parts_cost.setter
    def parts_cost(self, value):
        if value < 0:
            raise ValueError("Koszt części nie może być ujemny.")
        self._parts_cost = value

    @property
    def labor_hours(self):
        """Liczba roboczogodzin"""
        return self._labor_hours

    @labor_hours.setter
    def labor_hours(self, hours):
        if hours < 0:
            raise ValueError("Liczba roboczogodzin nie może być ujemna.")
        self._labor_hours = hours

    @property
    def labor_cost(self):
        """Koszt robocizny wyliczany dynamicznie"""
        return self._labor_hours * self.labor_rate

    @property
    def total_cost(self):
        """Całkowity koszt naprawy"""
        return self.parts_cost + self.labor_cost

    def __str__(self):
        return (f"Naprawa samochodu: {self.car_model}\n"
                f"Koszt części: {self.parts_cost} zł\n"
                f"Roboczogodziny: {self.labor_hours} h\n"
                f"Koszt robocizny: {self.labor_cost} zł\n"
                f"Całkowity koszt: {self.total_cost} zł")

# Przykład użycia:
repair = CarRepair("Audi A4")
repair.parts_cost = 1200
repair.labor_hours = 5  # 5 godzin pracy mechanika

print(repair)

# Test walidacji - odkomentuj, aby zobaczyć błąd:
# repair.parts_cost = -500  # ValueError: Koszt części nie może być ujemny
