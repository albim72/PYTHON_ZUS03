
class RunSession:
    def __init__(self, distance_km:float, time_minutes:float, calories_burned:int):
        self.distance_km = distance_km          # przebyty dystans w kilometrach
        self.time_minutes = time_minutes        # czas biegu w minutach
        self.calories_burned = calories_burned  # spalone kalorie

    def average_pace(self):
        """
        Oblicza średnie tempo biegu w minutach na kilometr
        """
        if self.distance_km == 0:
            return 0
        return self.time_minutes / self.distance_km
