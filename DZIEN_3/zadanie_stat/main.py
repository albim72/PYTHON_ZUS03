from runsession import RunSession

session = RunSession(distance_km=21.1, time_minutes=112.56, calories_burned=1128)

print(f"Dystans: {session.distance_km} km")
print(f"Czas: {session.time_minutes} minut")
print(f"Średnie tempo: {session.average_pace():.2f} min/km")

# Porównujemy spalone kalorie rzeczywiste z estymacją
cals = session.calories_burned
est = session.estimate_calories()
print(f"Rzeczywiste spalone kalorie: {cals} kcal")
print(f"Szacowane spalone kalorie: {est} kcal")
print(f"Różnica w spalaniu kcal (estymowana - rzeczywista): {est-cals} kcal")

# Test metody statycznej BMI
weight = 88  # kg
height = 172  # cm
bmi = RunSession.calculate_bmi(weight, height)
print(f"BMI dla wagi {weight} kg i wzrostu {height} cm wynosi: {bmi:.2f}")
