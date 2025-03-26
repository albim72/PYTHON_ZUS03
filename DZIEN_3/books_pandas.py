import pandas as pd

books = [
    {"title": "Wiedźmin", "author": "Andrzej Sapkowski", "year": 1993, "genre": "Fantasy"},
    {"title": "Lalka", "author": "Bolesław Prus", "year": 1890, "genre": "Powieść"},
    {"title": "Zbrodnia i kara", "author": "Fiodor Dostojewski", "year": 1866, "genre": "Powieść psychologiczna"}
]

#obiekty PANDAS -> Series [1D], DataFrame [2D]
df = pd.DataFrame(books)

#zapis DF do pliku json
df.to_json('books_pandas.json',orient='records',indent=4)
print("dane zapisano do pliku json")

#odczyt z pliku jSON
df_loaded = pd.read_json('books_pandas.json')

print("\n dane odczytane z pliku json:\n")
print(df_loaded)

print("operacje na danych DataFrame")
#dodanie kolumny z informacją ile lat ma książka
print("\nDODWANIE NOWEGO POLA\n")
current_year = 2025
df['book_age'] = current_year - df['year']

print(df)

print("\nFILTROWANIE - TYLKO KSIĄŻKI STARSZE NIŻ 100 LAT\n")
old_books = df[df['book_age']>100]
print(old_books)

print("\nSORTOWANIE - WEDŁUG ROKU WYDANIA\n")
sorted_books = df.sort_values(by='year')
print(sorted_books)

print("\nFILTROWANIE PO GATUNKU ZAWIERAJĄCE SŁOWO - POWIEŚC\n")
novels = df[df['genre'].str.contains('Powieść')]
print(novels)
