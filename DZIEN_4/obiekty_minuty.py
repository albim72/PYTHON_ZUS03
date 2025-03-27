class CzasTrwania:
    def __init__(self,godziny,minuty):
        self.godziny = godziny
        self.minuty = minuty

    def __str__(self):
        return f"{self.godziny}h {self.minuty} min"

    @classmethod
    def from_total_minutes(cls,total_minutes):
        godziny = total_minutes//60
        minuty = total_minutes%60
        return cls(godziny,minuty)

a = CzasTrwania(2,31)

b = CzasTrwania.from_total_minutes(127)

print(a)
print(b)
        
