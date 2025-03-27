from simpledt import Book,Author
from konferencja import Event
from datetime import datetime, timedelta

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

print("______ przykład 2 -> wyliczenie czasu trwania Eventu ________")
event1 = Event(
    name="Konferencja IntelliAI",
    start_date=datetime(2025,6,12,9,0),
    end_date=datetime(2025,6,16,18,30)
)
print(event1.descrption)

event2 = Event(
    name="Spotkanie projektowe",
    start_date=datetime(2025,5,10,17,15),
    end_date=datetime(2025,5,10,13,50)
)
print(event2.descrption)
