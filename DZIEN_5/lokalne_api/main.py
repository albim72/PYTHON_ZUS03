from fastapi import FastAPI, HTTPException
from .models import Book
from .data import books

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books", response_model=list[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    return book
