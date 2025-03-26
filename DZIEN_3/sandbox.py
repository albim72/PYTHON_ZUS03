import time

def sandbox(user_code):
    #tworzymy dozwolone wbudowane funkcje (bez open,exec,eval)
    safe_builtings = {
        'print':print,
        'range':range,
        'len':len,
        'sum':sum,
        'min':min,
        'max':max,
        'abs':abs,
    }

    local_namespace = {}

    #dodajemy tylko bezpieczne funkcje
    sandbox_globals = {
        '__builtins__':safe_builtings
    }

    #startujemy pomiar czasu
    start_time = time.time()

    try:
        exec(user_code,sandbox_globals,local_namespace)
    except Exception as e:
        return f"Sanbox error: {e}"

    exec_time = time.time() - start_time

    return local_namespace,exec_time


user_code ="""
result=[]
for i in range(10):
    result.append(i-10)
"""

namespace, duration = sandbox(user_code)
print(f"wynik: {namespace.get('result')}")
print(f"czas wykonania: {duration:.5f} s")
