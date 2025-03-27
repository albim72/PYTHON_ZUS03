from dataclasses import dataclass,field
from datetime import datetime, timedelta

@dataclass
class Event:
    name:str
    start_date:datetime
    end_date:datetime
    duration:timedelta = field(init=False)
    
    def __post_init__(self):
        if self.end_date < self.start_date:
            raise ValueError("Data zakończenia nie może byc wcześniejsza niż data rozpoczęcia")
        self.duration = self.end_date - self.start_date
        
    @property
    def descrption(self)->str:
        days = self.duration.days
        hours = self.duration.seconds//3600
        return (f'Wydarzenie "{self.name}" trwa {days} dni i {hours} godzin '
                f'(od {self.start_date} do {self.end_date}).')
