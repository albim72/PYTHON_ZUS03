# instalacja lokalnych pakietów -> pip install .
from textutils import clean_text,word_count
from textutils import processor

text = "Hello World! Welcome >> to the Python Package example."

cleaned = clean_text(text)
print(f"wyczyszczony tekst: {cleaned}")

print("_"*60)
print(processor.process("HELLO"))
