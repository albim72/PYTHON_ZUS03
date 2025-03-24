class RepairError(Exception):
    """Bazowy wyjątek dla błędów naprawy samochodu."""
    pass

class InvalidPartCostError(RepairError):
    """Wyjątek podnoszony, gdy koszt części jest nieprawidłowy."""
    def __init__(self, cost):
        super().__init__(f"Nieprawidłowy koszt części: {cost} zł. Koszt nie może być ujemny.")

class InvalidLaborHoursError(RepairError):
    """Wyjątek podnoszony, gdy liczba roboczogodzin jest nieprawidłowa."""
    def __init__(self, hours):
        super().__init__(f"Nieprawidłowa liczba roboczogodzin: {hours}. Wartość nie może być ujemna.")


class CarRepair:
    def __init__(self, car_model):
        self.car_model = car_model
        self._parts_cost = 0
        self._labor_hours = 0
        self.labor_rate = 150  # zł za godzinę robocizny

    @property
    def parts_cost(self):
        return self._parts_cost

    @parts_cost.setter
    def parts_cost(self, value):
        if value < 0:
            raise InvalidPartCostError(value)
        self._parts_cost = value

    @property
    def labor_hours(self):
        return self._labor_hours

    @labor_hours.setter
    def labor_hours(self, hours):
        if hours < 0:
            raise InvalidLaborHoursError(hours)
        self._labor_hours = hours

    @property
    def total_cost(self):
        return self._parts_cost + (self._labor_hours * self.labor_rate)


# Przykład użycia
try:
    repair = CarRepair("BMW X5")
    repair.parts_cost = 1500
    repair.labor_hours = -3  # Spowoduje błąd
except RepairError as e:
    print(f"Błąd naprawy: {e}")
