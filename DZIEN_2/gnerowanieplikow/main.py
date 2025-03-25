from report import Report
from csvgenerator import CsvGenerator
from jsongenerator import JsonGenerator
from pdfgenerator import PdfGenerator


#dane
sales_data = [
    {"produkt":"młot pneumatyczny","ilosc":4,"wartosc":1200},
    {"produkt":"rębak do drzewa","ilosc":1,"wartosc":12300},
    {"produkt":"piła elektryczna","ilosc":3,"wartosc":899},
]

report = Report()
report.add_generator(CsvGenerator())
report.add_generator(JsonGenerator())
report.add_generator(PdfGenerator())

report.export(sales_data)
