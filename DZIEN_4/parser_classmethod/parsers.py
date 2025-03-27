class Parser:
    _registry  = {} #rejestr wszystkich klas parserów

    def __init_subclass__(cls,format_name=None, **kwargs):
        """Automatyczna rejestracja klasy potomnej"""
        super().__init_subclass__(**kwargs)
        if format_name:
            Parser._registry[format_name] = cls

    def parse(self,text):
        raise NotImplementedError("Subklasa musi zaimplementowac metodę parse")

    @classmethod
    def create_parser(cls,format_name):
        """Tworzy instancję Parsera na podstawie formatu"""
        if format_name not in cls._registry:
            raise ValueError(f"Nieznany format: {format_name}")
        return cls._registry[format_name]()

#konkretny parser JSON
class JSONParser(Parser,format_name="json"):
    def parse(self,text):
        import json
        return json.loads(text)

#konkretny parser XML

class XMLParser(Parser,format_name="xml"):
    def parse(self,text):
        import xml.etree.ElementTree as ET
        return ET.fromstring(text)

