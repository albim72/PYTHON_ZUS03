from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    title:str
    author:str
    year:int
    cover_color:str

    @property
    def description(self)->str:
        return f"'{self.title}' autorstwa {self.author} ({self.year}, okładka: {self.cover_color})"
    
    def age(self)->str:
        current_year = datetime.now().year
        return current_year - self.year
    
