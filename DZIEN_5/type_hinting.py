def powitanie(imie:str,wiek:int) -> str:
    return f"Cześc {imie}, masz {wiek} lat"

print(powitanie("Piotr",45))
print(powitanie(True,11))
print(powitanie(3245234233,"dwa"))

from typing import List

def suma_liczb(liczby:List[int])->int:
    return sum(liczby)

print(suma_liczb([5,7,3,78,True]))
