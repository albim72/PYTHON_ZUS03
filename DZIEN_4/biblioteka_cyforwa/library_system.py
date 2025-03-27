from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Optional
import json

@dataclass
class Author:
    first_name: str
    last_name: str
    birth_year: int

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Book:
    title: str
    author: Author
    year: int
    isbn: str
    status: str = "available"
    borrow_date: Optional[datetime] = None

    def borrow(self):
        if self.status == "borrowed":
            raise ValueError("Książka jest już wypożyczona.")
        self.status = "borrowed"
        self.borrow_date = datetime.now()

    def return_book(self):
        if self.status == "available":
            raise ValueError("Książka nie jest wypożyczona.")
        self.status = "available"
        self.borrow_date = None

    @property
    def borrow_duration(self) -> Optional[int]:
        if self.status == "available" or self.borrow_date is None:
            return None
        return (datetime.now() - self.borrow_date).days

@dataclass
class User:
    first_name: str
    last_name: str
    borrowed_books: List[Book] = field(default_factory=list)

    def borrow_book(self, book: Book):
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Ta książka nie znajduje się na liście wypożyczonych przez użytkownika.")

# Funkcje pomocnicze do zapisu i wczytywania JSON

def serialize_to_json(authors: List[Author], books: List[Book], users: List[User], filename: str):
    def convert(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__dict__'):
            return asdict(obj)
        else:
            return str(obj)

    data = {
        "authors": [asdict(a) for a in authors],
        "books": [asdict(b) for b in books],
        "users": [
            {
                "first_name": u.first_name,
                "last_name": u.last_name,
                "borrowed_books": [b.isbn for b in u.borrowed_books]
            }
            for u in users
        ]
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, default=convert, indent=4, ensure_ascii=False)
