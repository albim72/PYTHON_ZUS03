import time
from functools import wraps

def mojdekorator(func):
    def wrapper():
        print(">> START FUNKCJI")
        func()
        print("<< KONIEC FUNKCJI")
    return wrapper

def info():
    print("to jest nowa informacja...")

z = mojdekorator(info)
z()

@mojdekorator
def greet():
    print("Witaj gościu...")

greet()


#dekorator mierzący czas i logujący dane

def log_and_time(func):
    @wraps(func) #zachowuje nazwę i dokumentcję funkcji
    def wrapper(*args,**kwargs):
        print(f"\n[LOG] Wywołanie funkcji: {func.__name__}")
        print(f"[LOG] Argumenty: {args}, Argumenty nazwane: {kwargs}")
        start_time = time.time()

        result = func(*args,**kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"[LOG] Wynik: {result}")
        print(f"[LOG] Czas wykonania: {duration:.4f} sekundy")
        return result
    return wrapper
