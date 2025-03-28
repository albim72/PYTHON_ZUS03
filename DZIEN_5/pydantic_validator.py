from pydantic import BaseModel,Field,EmailStr,conint,field_validator,ValidationError
from typing import Optional
from datetime import date,datetime

class Runner(BaseModel):
    first_name:str = Field(...,min_length=2)
    last_name:str
    email:EmailStr
    birth_date:date
    distance_km:conint(gt=0) #tylko dodatnie wartości
    club: Optional[str] = None

    @field_validator('birth_date')
    @classmethod
    def validate_age(cls,v:date)->date:
        today = date.today()
        age = today.year - v.year -((today.month,today.day)<(v.month,v.day))
        if age < 16:
            raise ValueError("Runner must be at least 16 years old")
        return v

    @property
    def age(self)->int:
        today = date.today()
        return (today.year - self.birth_date.year -
                ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))

data = {
    "first_name":"Jan",
    "last_name":"Kowalski",
    "email":"jan.kowalski@cos.pl",
    "birth_date":"1976-04-15",
    "distance_km":45,
    "club":"Banda Grzesia"
}

runner = Runner(**data)
print(runner)
# Pass the birth_date attribute of the runner object which is a date object
print(runner.validate_age(runner.birth_date))
print(runner.age)
