# --- Przykład: zarządanie biblioteką w Pythonie ----

# Lista(list) -> lista książek w bibliotece
# CTRL+D -> powielanie linii/bloku

books = [
    ("Wiedźmin","Andrzej Sapkowski",1990),
    ("Pan Tadeusz","Adam Mickiewicz",1834),
    ("Lalka","Bolesław Prus",1890),
    ("Quo Vadis","Henryk Sienkiewicz",1896),
    ("Faraon","Bolesław Prus",1897)
]

# Krotka(tuple): stała reprezentująca godziny otwarcia

opening_hours = ("9:00","17:00")

#Zbiór(set): zbiór unikalnych autorów
authors = set()

#Słownik(dict): książki napisane przez wybranego autora
library_by_author = {}

print(f"Godziny otwarcia biblioteki: {opening_hours[0]} - {opening_hours[1]}\n")
