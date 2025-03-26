from dataclasses import dataclass
from datetime import date

@dataclass
class Book:
    title:str
    author:str
    published_year:int
    pages:int
    binding:str = "Paperback"

    #jawne wypisanie funkcji init doprowadza do destrukcji domyślnego init() zbudowanego na bazie zdefiniowanych pól
    # def __init__(self,isbn):
    #     self.isbn= isbn

    def age(self)->int:
        current_year = date.today().year
        return current_year - self.published_year

#tworzenie obiektu klasy Book
book = Book(title="1984",author="George Orwell",published_year=1949,pages=328)

print(book)
print(f"wiek książki: {book.age()} lat")

book2 = Book(title="Wiedżmin",author="Andrzej Sapkowski",published_year=1986,pages=345,binding="Hardcover")
print(book2)
print(f"wiek książki: {book2.age()} lat")
