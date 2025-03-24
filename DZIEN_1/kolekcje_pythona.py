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

#dodanie autorów do zbioru i organizacja książek w słowniku
for title,author,year in books:
    authors.add(author)
    if author not in library_by_author:
        library_by_author[author] = []
    library_by_author[author].append((title,year))

#lista książek w bibliotece
for title,author,year in books:
    print(f" - '{title}' ({year}), autor: {author}")

# Unikalni autorzy w bibliotece
print("\nUnikalni autorzy w bibliotece:")
for author in authors:
    print(f" - {author}")

# Książki według autorów
print("\nKsiążki według autorów:")
for author,titles in library_by_author.items():
    print(f"\nAutor: {author}")
    for title,year in titles:
        print(f" -> '{title}' ({year})")
