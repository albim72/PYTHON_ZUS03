"""
Skonstrruj contexmanagera: CSVFileManager, którego implementacja pozwoli na:
1. Odczyt danych z pliku CSV i zwrócenie ich w postaci listy słowników
2. Zapis danych do pliku CSV na podstawie podanej listy słowników
3. Filtrowanie danych z pliku CSV na podstawie określonrgo warunku

"""

import csv

class CSVManager:
    def __init__(self,file_name):
        self.file_name = file_name

    def read_csv(self):
        data = []
        with open(self.file_name,mode='r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data

    def write_csv(self,data,headers=None):
        with open(self.file_name,mode='w',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            if headers:
                writer.writeheader()
            for row in data:
                writer.writerow(row)

    def filter_csv(self,condition):
        filtered_data = []
        with open(self.file_name,mode='r',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if condition(row):
                    filtered_data.append(row)
        return filtered_data

file_manager = CSVManager('osoby.csv')

#odczyt danych z pliku csv
data = file_manager.read_csv()
print("Dane z pliku csv")
print(data)

#zapis danych do pliku
new_data = [{'Imie':'Jerzy','Wiek':37},{'Imie':'Eliza','Wiek':29},{'Imie':'Vera','Wiek':42}]

file_manager.write_csv(new_data,headers=['Imie','Wiek'])

#filtorwanie i odczyt
filtered_data = file_manager.filter_csv(lambda row:int(row['Wiek'])>30)
print("Filtowanie danych z pliku CSV:")
print(filtered_data)
