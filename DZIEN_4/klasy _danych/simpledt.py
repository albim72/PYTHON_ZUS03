from dataclasses import dataclass

@dataclass
class Book:
    title:str
    author:str
    year:int
    cover_color:str
    
    @property
    def description(self)->str:
        return f"'{self.title}' autorstwa {self.author} ({self.year}, okładka: {self.cover_color})"
