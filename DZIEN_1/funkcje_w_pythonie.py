#przykład 1 -> prosta funkcja matematyczna
#silnia(n) = 1*2*3*...*n, dla n >= 0
def factorial(n):
    if n==0 or n==1:
        return 1
    #funkcja rekurencyjna
    return n*factorial(n-1)

print(f"Silnia z 7 wynosi: {factorial(7)}")

#przykład 2 - funkcja przetwarzająca listę /filtrowanie liczb parzystch/
def filter_even(numbers):
    return [num for num in numbers if num%2==0]
    #list comprehension  - rodzaj funkcji anonimowej zamknięty wewnątrz kolekcji

liczby = [5,2,8,3,23,78,9,32,6,8,0,-23,57,43,68,44,66,11,12]
print(filter_even(liczby))

#przykład 3 - funkcja operująca na słowniku - zliczanie wystąpień słów
def word_count(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    return counts

print(word_count("Hello world hello Python Python world Hello everybody"))
