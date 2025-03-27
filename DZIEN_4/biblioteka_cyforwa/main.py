if __name__ == "__main__":
    author1 = Author("George", "Orwell", 1903)
    author2 = Author("Harper", "Lee", 1926)

    book1 = Book("1984", author1, 1949, "123-A")
    book2 = Book("To Kill a Mockingbird", author2, 1960, "456-B")

    user = User("Jan", "Kowalski")

    user.borrow_book(book1)

    print(book1.borrow_duration)  # np. 0
    print(book1.status)  # borrowed

    user.return_book(book1)
    print(book1.status)  # available

    serialize_to_json([author1, author2], [book1, book2], [user], "library_data.json")
