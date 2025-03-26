class RunSession:
    CALORIES_PER_KM = 60  # Stała: średnie spalanie kcal na 1 km

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

    def estimate_calories(self):
        """
        Szacuje spalone kalorie na podstawie przebytego dystansu
        """
        return self.distance_km * RunSession.CALORIES_PER_KM

    @staticmethod
    def calculate_bmi(weight_kg, height_cm):
        """
        Statyczna metoda obliczająca BMI
        BMI = waga (kg) / (wzrost (m))^2
        """
        if height_cm == 0:
            return 0
        height_m = height_cm / 100
        return weight_kg / (height_m ** 2)
