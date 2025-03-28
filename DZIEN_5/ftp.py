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

ftp.quit()
