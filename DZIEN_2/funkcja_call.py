class MojeCall:
    def __init__(self,value):
        self.value = value

    def __call__(self,x):
        return self.value*x

ob = MojeCall(45)
print(ob)
print(ob.__call__(3))

print(ob(9))

print("_"*60)

class DataValidator:
    def __init__(self):
        self.cache = {}

    def validate(self,data):
        print(f"Waliduję dane: {data}")
        if not isinstance(data,str):
            raise ValueError("Dane muszą byc tekstem!")
        if len(data) < 3:
            raise ValueError("Dane są za krótkie")
        return True

    def __call__(self,data):
        if data in self.cache:
            print(f"Cache HIT dla: {data}")
            return self.cache[data]
        try:
            wynik = self.validate(data)
            self.cache[data] = wynik
            return wynik
        except ValueError as e:
            print(f"błąd walidacji: {e}")
            self.cache[data] = False
            return False

validator = DataValidator()
print(validator("Janek"))
print(validator("Jan"))
print(validator("Ja"))
print(validator(1234))
print(validator("Jan"))
print(validator("Janek"))
print(validator(1234))
