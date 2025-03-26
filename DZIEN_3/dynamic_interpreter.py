def run_user_code(user_code):
    #tworzymy izolowany namespace jako pusty słownik
    local_namespace = {}

    #uruchamiamy kod użytkownika w naszym lokalnym namespace
    exec(user_code,{},local_namespace)

    #możemy wydobyc tylko to co powstało w lokalnym namespace
    return local_namespace

user_code = """
result = []
for i in range(5):
    result.append(i*8)
"""

namespace = run_user_code(user_code)
print(namespace['result'])

print("_"*60)
#dynamiczny import modułu w osobnym namespace
def dynamic_import(module_name):
    module_namespace = {}
    exec(f"import {module_name}",module_namespace)

    return module_namespace


namespace = dynamic_import('math')
print(namespace['math'].sqrt(16))


# print(math.sqrt(23))

print("_"*60)
#tworzenie i użycie klasy w osobnym namespace

def run_user_class():
    user_code = '''
class Greeter:
    def __init__(self,name):
        self.name = name
            
    def greet(self):
        return f"Hello, {self.name}!"
greeter = Greeter("Maria")
result = greeter.greet()
    '''
    local_namesapce = {}
    exec(user_code,{},local_namesapce)
    return local_namesapce['result']

print(run_user_class())
