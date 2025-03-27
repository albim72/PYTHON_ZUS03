import xml.sax

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.title = ""
        self.author = ""
        self.year = ""
        self.isbn = ""
        self.books = []

    def startElement(self, tag, attributes):
        self.current_data = tag

    def characters(self, content):
        if self.current_data == "title":
            self.title += content
        elif self.current_data == "author":
            self.author += content
        elif self.current_data == "year":
            self.year += content
        elif self.current_data == "isbn":
            self.isbn += content

    def endElement(self, tag):
        if tag == "book":
            self.books.append({
                "title": self.title.strip(),
                "author": self.author.strip(),
                "year": self.year.strip(),
                "isbn": self.isbn.strip()
            })
            self.title = ""
            self.author = ""
            self.year = ""
            self.isbn = ""
        self.current_data = ""

def parse_large_xml_sax(file_path="large_books.xml"):
    handler = BookHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler.books

# Parsowanie i wyświetlenie wyników
books_parsed = parse_large_xml_sax()

# Można wypisać np. pierwsze 5
for book in books_parsed[:5]:
    print(book)
