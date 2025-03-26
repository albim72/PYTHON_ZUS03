#analiza namespaces
import runners
from types import SimpleNamespace

x = 100 #przestrzeń globalna
def costam():
    y = 5 #przestrzeń lokalna
    print(y,x)
    def info():
        r = "takie" #enclosing
        print(r)

costam()
print("to jest przestrzeń built-in (print())")

print("*"*70)

print("__przestrzeń jako plik pythona__")
runner = runners.Runner("Jan Kowalski")
print(runner.name)


print("__przestrzeń jako klasa pythona__")
class RaceNamespace:
    race_name = "Tatra Sky Marathon"
    distance_km =45
    elevation_gain = 3500

print(RaceNamespace.race_name)
print(RaceNamespace.distance_km)

print("__przestrzeń jako typ types.SimpleNamespace__")

race = SimpleNamespace()
race.name = "Tatra Sky Marathon"
race.distance_km =45
race.elevation_gain = 3500

print(race.distance_km)

print("__przestrzeń jako typ dict__")
race = {
    "race_name":"Tatra Sky Marathon",
    "distance_km":45,
    "elevation_gain":3500
}
print(race["race_name"])
