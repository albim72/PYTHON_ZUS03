from dataclasses import dataclass
from datetime import datetime

@dataclass
class Author:
    first_name:str
    last_name:str
    
    def full_name(self)->str:
        return f"{self.first_name} {self.last_name}"

@dataclass
class Book:
    title:str
    year:int
    cover_color:str
    author:Author

    @property
    def description(self)->str:
        return f"'{self.title}' autorstwa {self.author.full_name()} ({self.year}, okładka: {self.cover_color})"

    def age(self)->str:
        current_year = datetime.now().year
        return current_year - self.year
