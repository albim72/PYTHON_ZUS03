import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect("dane.db")
df = pd.read_sql("SELECT * FROM pracownicy",conn)
conn.close()

#sortowanie po pensji malejąco
df_sorted = df.sort_values(by="salary",ascending=False)

print("posrtowna tabela ->\n")
print(df_sorted)

#filtrowanie -> osoby w wieku 30-45 lat z pensją >60000
df_filtered = df[(df['age']>=30)&(df['age']<=45) & (df['salary']>60000)]

print("_"*70)
print(df_filtered.to_string(index=False))

#wizualizacja - wykres pensji
plt.figure(figsize=(10,6))
plt.bar(df_sorted['name'],df_sorted['salary'])
plt.xticks(rotation=90)
plt.xlabel('Imię i nazwisko')
plt.ylabel('Pensja')
plt.title('Pensje pracowników (malejąco)')
plt.tight_layout()
plt.show()
