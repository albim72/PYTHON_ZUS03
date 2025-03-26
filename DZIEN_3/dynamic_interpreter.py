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
