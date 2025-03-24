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
