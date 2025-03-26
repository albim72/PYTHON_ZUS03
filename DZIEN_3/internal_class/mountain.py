def mountain_race_event(race_name,distance_km,elevation_gain,runners_data):
    class Runner:
        def __init__(self,name,age,category):
            self.name = name
            self.age = age
            self.category = category

        def __str__(self):
            return f"{self.name} ({self.age})  kategoria {self.category})"

    class Result:
        def __init__(self,runner,time_hours):
            self.runner = runner
            self.time_hours = time_hours

        def pace(self):
            return round((distance_km/self.time_hours),2)

        def __str__(self):
            return f"{self.runner} - {self.time_hours}h,  średnia prędkośc {self.pace()} km/h)"
        
    print(f"Zawody: {race_name} | Dystans {distance_km} km | Przewyższenie: {elevation_gain} m")
    #przetwarzanie danych zawodników
    for data in runners_data:
        runner = Runner(data['name'], data['age'],data['category'])
        result = Result(runner,data['time_hours'])
        print(result)
