import cProfile
import time

def slow_function():
    print("Start slow_function()")
    time.sleep(1)
    total = 0
    for i in range(1,1_000_000):
        total+=i**0.5
    print("End slow_function()")
    return total

def fast_function():
    print("Start fast_function()")
    total = sum([i**0.5 for i in range(1,100_000)])
    print("End fast_function()")
    return total

def main():
    slow_function()
    fast_function()

cProfile.run('main()')

cProfile.run('main()',filename='profiling_result.prof')

# intalacja snakeviz: pip install snakeviz

# uruchomienie obrazu prof - snakeviz: snakeviz profiling_result.prof
