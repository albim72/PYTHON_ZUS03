import json

def save_books(books, filename):
    with open(filename, 'w') as f:
        json.dump(books, f, indent=4)

def load_books(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    # Przykładowa lista książek
    books = [
        {"title": "Wiedźmin", "author": "Andrzej Sapkowski", "year": 1993, "genre": "Fantasy"},
        {"title": "Lalka", "author": "Bolesław Prus", "year": 1890, "genre": "Powieść"},
        {"title": "Zbrodnia i kara", "author": "Fiodor Dostojewski", "year": 1866, "genre": "Powieść psychologiczna"}
    ]

    # Zapis do pliku JSON
    save_books(books, 'books.json')
    print("Dane zapisano do pliku books.json")

    # Odczyt z pliku
    loaded_books = load_books('books.json')
    print("\nOdczytane dane z pliku:\n")
    for book in loaded_books:
        print(f"\"{book['title']}\" autor: {book['author']}, Rok: {book['year']}, Gatunek: {book['genre']}")

if __name__ == "__main__":
    main()
