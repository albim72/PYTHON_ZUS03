Przykład 1: Zdalne zarządzanie serwerem przez SSH (Paramiko)
import paramiko

# Dane dostępowe
host = '192.168.1.100'
port = 22
username = 'admin'
password = 'twoje_haslo'

# Tworzenie klienta SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Połączenie
ssh.connect(host, port=port, username=username, password=password)

# Wykonanie komendy
stdin, stdout, stderr = ssh.exec_command('uptime')
print("Wynik komendy:", stdout.read().decode())

# Zamykanie połączenia
ssh.close()


Przykład 2: Upload i wykonanie skryptu na serwerze

import paramiko

host = '192.168.1.100'
username = 'admin'
password = 'twoje_haslo'

# Połączenie
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password)

# Przesłanie pliku (np. skryptu)
sftp = ssh.open_sftp()
sftp.put('lokalny_skript.sh', '/tmp/skrypt.sh')
sftp.chmod('/tmp/skrypt.sh', 0o755)
sftp.close()

# Uruchomienie skryptu
stdin, stdout, stderr = ssh.exec_command('bash /tmp/skrypt.sh')
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()

#Alternatywa: fabric
from fabric import Connection

conn = Connection(host='admin@192.168.1.100', connect_kwargs={'password': 'twoje_haslo'})

# Uruchom komendę
result = conn.run('df -h', hide=True)
print(result.stdout)

# Prześlij plik
conn.put('lokalny.txt', '/home/admin/zdalny.txt')
