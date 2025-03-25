class FileManager:
    def __init__(self,filename,mode,enc):
        self.filename = filename
        self.mode = mode
        self.enc = enc
        self.file = None

    def __enter__(self):
        print("otwieram plik....")
        self.file = open(self.filename,self.mode,encoding=self.enc)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("zamykam plik")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"mamy wyjątek: {exc_val}")
            return True

with FileManager('test.txt','w','utf-8') as f:
    f.write("przykłada działania FileManager!")
    raise ValueError("Błąd testowy")

