class UnitConverter:
    @staticmethod
    def km_to_miles(km):
        return km*0.621371

    @staticmethod
    def miles_to_km(miles):
        return miles/0.621371

    @staticmethod
    def kg_to_pounds(kg):
        return kg*2.20462

    @staticmethod
    def pounds_to_kg(pounds):
        return pounds/2.20462


dist_km = 10
dist_miles = UnitConverter.km_to_miles(dist_km)
print(f"{dist_km} km to {dist_miles} mil")

weight_kg = 88
weight_pounds = UnitConverter.kg_to_pounds(weight_kg)
print(f"{weight_kg} kg to {weight_pounds:.2f} funtów")

#odwrotne przeliczenia
print(f"15 mil to {UnitConverter.miles_to_km(15):.2f} km")
print(f"221 funtów to {UnitConverter.pounds_to_kg(221):.2f} kg")
