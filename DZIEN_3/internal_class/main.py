from ccreate import create_class
from valid import validator_factory

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
