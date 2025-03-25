import re

def clean_text(text):
    """Usuwa znaki specjalne i zmienia tekst na małe litery"""
    text = re.sub(r'[^\w\s]','',text)
    return text.lower()
