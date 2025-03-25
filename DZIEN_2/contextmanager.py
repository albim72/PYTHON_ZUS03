class ContextManager:
    def __init__(self):
        print("wywołanie funkcji init()")

    def __enter__(self):
        print("wywołanie funkcji enter()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("wywołanie funkcji exit()")

with ContextManager() as manager:
    print("wykonanie bloku with...")
