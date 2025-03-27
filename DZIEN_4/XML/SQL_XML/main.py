#instalacja bibliotek -> pip install pandas numpy lxml
import pandas as pd
import numpy as np
import sqlite3

#wczytanie danych z pliku xml
xml_file = 'dane_osobowe.xml'

#parsowanie xml do DataFrame
df = pd.read_xml(xml_file,xpath='.//record')

#użyjmy numpy dp dodatkowego przetwarzania - standaryzacja kolumny salary
df['salary_standardized'] = (df['salary']-np.mean(df['salary']))/np.std(df['salary'])

#połączenie z bazą SQLITE - jeśli baza w formie pliku nie istniej - zostaje automatycznie utworzona
conn = sqlite3.connect('dane.db')

#zaapis danych do tabeli pracownicy
df.to_sql('pracownicy',conn,if_exists='replace',index=False)

print("dane zostały zapisane do bazy SQL")

#odczyt danych z tabeli
df_sql = pd.read_sql('SELECT * FROM pracownicy',conn)

conn.close()

#zamknięcie połączenia
print(df_sql)
