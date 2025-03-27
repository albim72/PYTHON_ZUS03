import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import random

def generate_large_xml(file_path="large_books.xml", count=200):
    titles = ["Book A", "Book B", "Book C", "Book D", "Book E"]
    authors = ["Author X", "Author Y", "Author Z", "Author W", "Author V"]
    library = ET.Element("library")

    for i in range(count):
        book_elem = ET.SubElement(library, "book")
        ET.SubElement(book_elem, "title").text = random.choice(titles) + f" #{i+1}"
        ET.SubElement(book_elem, "author").text = random.choice(authors)
        ET.SubElement(book_elem, "year").text = str(random.randint(1900, 2024))
        ET.SubElement(book_elem, "isbn").text = f"{i+1000}-X"

    xml_str = ET.tostring(library, encoding="utf-8")
    pretty_xml = parseString(xml_str).toprettyxml(indent="  ")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

generate_large_xml()
