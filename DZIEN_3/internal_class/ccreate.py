def create_class(name):
    #funkcja do tworzenia nowej klasy
    class DynamicClass:
        def __init__(self):
            self.name = name

        def greet(self):
            return f"Witaj użytkowniku {self.name}"

    return DynamicClass()
