from ccreate import create_class
from valid import validator_factory
from mountain import mountain_race_event

obj = create_class("Alicja")
print(obj.greet())

print("_"*60)

schema = {"name":str,"age":int}
Validator = validator_factory(schema)

data = {"name":"Janusz","age":"dwadzieścia"}
validator = Validator(data)

if not validator.validate():
    print(f"Błędy walidacji: {validator.get_errors()}")
else:
    print("Dane poprawne!")

data = {"name":"Anna","age":67}
validator = Validator(data)

if not validator.validate():
    print(f"Błędy walidacji: {validator.get_errors()}")
else:
    print("Dane poprawne!")

print("_"*60)

runners = [
    {"name":"Jan Kowalski","age":35,"category":"M30","time_hours":6.5},
    {"name":"Anna Nowak","age":62,"category":"M60","time_hours":8.45},
    {"name":"Marian Kruk","age":51,"category":"M50","time_hours":5.33}
]

#wywołanie funkcji
mountain_race_event("Tatra Sky Marathon",45,3500,runners)

