import os
from ftplib import FTP

#połączenie z zpublicznym serwerem testowym
ftp = FTP('test.rebex.net')
ftp.login(user='demo',passwd='password')

#Wpisanie plików i katalogów w katalogu głównym
ftp.retrlines('LIST')

#pobranie przykładowego pliku z serwera
filename = 'readme.txt'
with open(filename,'wb') as f:
    ftp.retrbinary(f'RETR {filename}',f.write)


#blok 2
#przejście do katalogu
ftp.cwd('/pub/example/')

#pobranie listy plików
plik_lista = []
ftp.retrlines('NLST',plik_lista.append) #tylko nazwy plików

print("Pliki w katalogu -> /pub/example/:")
for plik in plik_lista:
    print(f" - {plik}")

#tworzymy lokalny katalog na pobrane pliki
os.makedirs('pobrane',exist_ok=True)

#pobieranie plików z katalogu
for plik in plik_lista:
    lokalna_sciezka = os.path.join('pobrane',plik)
    with open(lokalna_sciezka,'wb') as f:
        ftp.retrbinary(f'RETR {plik}',f.write)
        print(f"pobrano plik: {plik}")

#dodanie pliku na serwer ftp

plik_lokalny = 'informacja.txt'

with open(plik_lokalny,'rb') as f:
    ftp.storbinary(f'STOR informacja.txt',f)
    print("plik został wysłany")

ftp.quit()
