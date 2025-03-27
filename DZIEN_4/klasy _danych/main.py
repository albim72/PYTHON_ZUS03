from simpledt import Book,Author

print("______ przykład 1 -> prosta dataclass Book ________")

orwell = Author("George","Orwell")
lee = Author("Harper","Lee")
huxley = Author("Aldous","Huxley")
sapkowski = Author("Andrzej","Sapkowski")

books = [
    Book("1984",1949,"czerwona",orwell),
    Book("To Kill a Mockingbird",1960,"niebieska",lee),
    Book("Brave New World",1932,"zielona",huxley),
    Book("Wiedźmin",1986,"czerwono-czarna",sapkowski),
    Book("Folwark zwierzęcy",1945,"żółta",orwell)
]

#opisy książek
books_sorted = sorted(books,key=lambda b: b.author.last_name)

print("Książki posortowane według nazwiska autora:\n")
for book in books_sorted:
    print(book.description)
    print(f"wiek książki: {book.age()} lat")
    print("*"*60)
