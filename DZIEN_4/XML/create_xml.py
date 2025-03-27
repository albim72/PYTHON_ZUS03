import xml.etree.ElementTree as ET
from xml.dom import minidom


books = [
    {"title":"1984","author":"Geroge Orwell","year":"1949","isbn":"123-A"},
    {"title":"To Kill a Mockingbird","author":"Harper Lee","year":"1960","isbn":"456-B"},
    {"title":"Brave New World","author":"Aldoux Huxley","year":"1932","isbn":"789-C"},
    {"title":"Wiedźmin","author":"Andrzej Sapkowski","year":"1986","isbn":"732-G"}
]

library = ET.Element("library")

for book in books:
    book_elem = ET.SubElement(library,"book")
    ET.SubElement(book_elem,"title").text = book["title"]
    ET.SubElement(book_elem,"author").text = book["author"]
    ET.SubElement(book_elem,"year").text = book["year"]
    ET.SubElement(book_elem,"isbn").text = book["isbn"]

#funkcja ładnego formatowania (pretty print)
def prettify(elem:ET.Element)->str:
    rough_string = ET.tostring(elem,encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="   ")

#zapis do pliku z formatowaniem
xml_string = prettify(library)

with open("books_generated.xml","w",encoding="utf-8") as f:
    f.write(xml_string)

print("plik został wygenerowany!")
