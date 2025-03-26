class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" — {self.author} ({self.year})'


class Library:
    def __init__(self):
        self.books = []

    def __add__(self, book):
        """Dodaje obiekt Book do biblioteki za pomocą operatora +"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Do biblioteki można dodać tylko obiekt klasy Book")
        return self

    def __call__(self, keyword):
        """Wyszukiwanie książek po słowie kluczowym"""
        result = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                result.append(book)
        return result

    def save_to_file(self, filename):
        """Zapisuje książki do pliku tekstowego"""
        with open(filename, 'w', encoding='utf-8') as file:
            for book in self.books:
                file.write(f"{book.title};{book.author};{book.year}\n")

    def load_from_file(self, filename):
        """Wczytuje książki z pliku tekstowego"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(';')
                    if len(parts) == 3:
                        title, author, year_str = parts
                        try:
                            year = int(year_str)
                            self.books.append(Book(title, author, year))
                        except ValueError:
                            print(f"Nieprawidłowy rok wydania w linii: {line.strip()}")
        except FileNotFoundError:
            print(f"Plik {filename} nie istnieje.")

    def remove_book(self, title):
        """Usuwa książkę z biblioteki po tytule"""
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Książka "{title}" została usunięta z biblioteki.')
                return
        print(f'Nie znaleziono książki o tytule "{title}".')

if __name__ == "__main__":
    library = Library()
    library + Book("Duma i uprzedzenie", "Jane Austen", 1813)
    library + Book("Władca Pierścieni", "J.R.R. Tolkien", 1954)
    library + Book("Hobbit", "J.R.R. Tolkien", 1937)

    print("Przed usunięciem:")
    for book in library.books:
        print(book)

    library.remove_book("Hobbit")

    print("\nPo usunięciu Hobbita:")
    for book in library.books:
        print(book)

    #zapis do pliku
    library.save_to_file("biblio.txt")

    #wczytanie z pliku
    new_library = Library()
    new_library.load_from_file("second.txt")
    print("\nbiblioteka wczytana z pliku:\n")
    for book in new_library.books:
        print(book)
