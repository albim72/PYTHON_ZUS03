import requests

BASE_URL = "http://127.0.0.1:8000"

def get_all_books():
    response = requests.get(f"{BASE_URL}/books")
    if response.status_code == 200:
        books = response.json()
        print("📚 Lista książek:")
        for book in books:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("❌ Błąd podczas pobierania książek")

def get_book_by_id(book_id):
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    if response.status_code == 200:
        book = response.json()
        print(f"📘 Książka {book_id}: {book['title']} ({book['year']})")
    else:
        print(f"❌ Książka o ID {book_id} nie istnieje")

def add_new_book(book_data):
    response = requests.post(f"{BASE_URL}/books", json=book_data)
    if response.status_code == 200:
        book = response.json()
        print(f"✅ Dodano książkę: {book['title']} ({book['id']})")
    else:
        print(f"❌ Błąd dodawania książki: {response.json()['detail']}")

if __name__ == "__main__":
    get_all_books()
    
    print("\n➡ Dodajemy nową książkę...")
    new_book = {
        "id": 4,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy"
    }
    add_new_book(new_book)

    print("\n➡ Pobieramy książkę o ID 4:")
    get_book_by_id(4)
