import paramiko
from scp import SCPClient

# Dane dostępowe do serwera
host = '192.168.1.100'         # adres IP lub domena
port = 22                      # port SSH
username = 'jan'               # nazwa użytkownika
password = 'twoje_haslo'       # hasło lub użyj klucza

# Ścieżka do pliku lokalnego i docelowego
local_file = 'plik.txt'
remote_path = '/home/jan/'

# Tworzenie połączenia SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)

# Tworzenie klienta SCP
with SCPClient(ssh.get_transport()) as scp:
    scp.put(local_file, remote_path=remote_path)
    print("Plik został wysłany przez SCP.")

# Zamknięcie połączenia
ssh.close()
