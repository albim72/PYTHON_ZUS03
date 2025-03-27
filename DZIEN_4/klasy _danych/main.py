from simpledt import Book

print("______ przykład 1 -> prosta dataclass Book ________")
book1 = Book("1984","George Orwell",1949,"czerwona")
book2 = Book("To Kill a Mockingbird","Harper Lee",1960,"niebieska")
book3 = Book("Brave New World","Aldous Huxley",1932,"zielona")
book4 = Book("Wiedźmin","Andrzej Sapkowski",1986,"czerwono-czarna")

#opisy książek
for book in (book1,book2,book3,book4):
    print(book.description)
    print(f"Wiek książki: {book.age()} lat\n")
    print("*"*60)
