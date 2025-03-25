import os
#odczyt pliku
with open('dane.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(f"Zawartośc pliku:\n{content}")

#dopisywanie do pliku
with open('dane.txt','a',encoding='utf-8') as f:
    f.write("\nPiąta linia (dodana)")

#nadpisywanie/tworzenie pliku
with open('dane.txt','w',encoding='utf-8') as f:
    f.write("Plik został nadpisany\nNowa zawartośc")

with open('abc.txt','w',encoding='utf-8') as f:
    f.write("Plik został utworzony\nnowy plik abc.txt")

#odczyt wiersz po wierszu
with open('dane.txt','r',encoding='utf-8') as f:
    for line in f:
        print(f">{line.strip()}")

#odczyt jako lista linii
with open('dane.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

#odczyt/zapis binarny
with open('dane.txt','rb') as f:
    binary_content = f.read()
    print(binary_content)

with open('cdane.txt','wb') as f:
    f.write(binary_content)

#obsługa wyjątków - błędy
try:
    with open("brak.txt",'r',encoding='utf-8') as f:
        data = f.read()
except FileNotFoundError:
    print("Plik nie istnieje!")
else:
    print(data)
finally:
    if not os.path.exists('brak.txt'):
        with open("nowybrak.txt",'w',encoding='utf-8') as f:
            f.write("plik utworzony w finally!!!")
        print("Plik nowybrak.txt został utworzony!")
