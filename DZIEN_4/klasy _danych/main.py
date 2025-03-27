from simpledt import Book

print("______ przykład 1 -> prosta dataclass Book ________")
book1 = Book("1984","George Orwell",1949,"czerwona")
book2 = Book("To Kill a Mockingbird","Harper Lee",1960,"niebieska")
book3 = Book("Brave New World","Aldous Huxley",1932,"zielona")
book4 = Book("Wiedźmin","Andrzej Sapkowski",1986,"czerwono-czarna")

#opisy książek
print(book1.description)
print(book2.description)
print(book3.description)
print(book4.description)
