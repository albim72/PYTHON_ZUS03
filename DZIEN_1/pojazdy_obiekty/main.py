import os #biblioteki wbudowane w interpreter pythona
import numpy as np #biblioteki trzecie - zewnętrzne
from samochod import Samochod #biblioteki własne
#biblioteki == moduły(pliki pythona)

moj_samochod = Samochod("BMW","czarny")
moj_samochod.jedz()
moj_samochod.info()
print(moj_samochod)

twoj_samochod = Samochod("Toyota","czerwony")
twoj_samochod.jedz()
twoj_samochod.info()
print(twoj_samochod)
