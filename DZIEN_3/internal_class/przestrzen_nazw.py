#analiza namespaces
x = 100 #przestrzeń globalna
def costam():
    y = 5 #przestrzeń lokalna
    print(y,x)
    def info():
        r = "takie" #enclosing
        print(r)

costam()
print("to jest przestrzeń built-in (print())")
