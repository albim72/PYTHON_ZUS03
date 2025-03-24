#przykład 1 -> prosta funkcja matematyczna
#silnia(n) = 1*2*3*...*n, dla n >= 0
def factorial(n):
    if n==0 or n==1:
        return 1
    #funkcja rekurencyjna
    return n*factorial(n-1)

print(f"Silnia z 7 wynosi: {factorial(7)}")
