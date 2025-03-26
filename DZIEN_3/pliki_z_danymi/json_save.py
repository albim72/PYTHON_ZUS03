import json

def save_race_results(runners, filename):
    with open(filename, 'w') as f:
        json.dump(runners, f, indent=4)

def load_race_results(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    # Przykładowe dane zawodników
    runners = [
        {"name": "Jan Kowalski", "age": 35, "category": "M30", "time_hours": 6.5},
        {"name": "Anna Nowak", "age": 29, "category": "K30", "time_hours": 7.2},
        {"name": "Piotr Zalewski", "age": 42, "category": "M40", "time_hours": 7.0}
    ]

    # Zapis do pliku JSON
    save_race_results(runners, 'race_results.json')

    print("\nWyniki zapisane w pliku 'race_results.json'. Teraz odczytuję i sortuję wyniki...\n")

    # Odczyt i sortowanie wyników
    loaded_runners = load_race_results('race_results.json')
    sorted_runners = sorted(loaded_runners, key=lambda x: x['time_hours'])

    # Wyświetlenie posortowanych wyników
    for runner in sorted_runners:
        print(f"{runner['name']} ({runner['category']}) - czas: {runner['time_hours']} h")

if __name__ == "__main__":
    main()
