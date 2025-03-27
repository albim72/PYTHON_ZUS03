import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

print("Lista książek:\n")
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    year = book.find("year").text
    isbn = book.find("isbn").text

    print(f"Tytuł {title}")
    print(f"Autor: {author}")
    print(f"Rok wydania: {year}")
    print(f"ISBN: {isbn}")
    print("_"*50)
