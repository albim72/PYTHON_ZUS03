"""
Funkcja wyższego rzędu -> process_documents()
funkcja przyjmuje listę dokumentów -> artykułów, postów, recenzji...
Następnie wykonuje dodatkową agregację wyników.
Złożonośc: O(N*M*f(M)), gdzie N - liczba dokumentów, M - średnia długośc dokumentu,
f(M) -> funkcja złożonej analizy
"""

from typing import List,Callable,Dict
from collections import Counter
from functools import partial
import re

def process_documents(docs:List[str],analisys_fn:Callable[[str],Dict[str,int]]) -> Dict[str,int]:
    """
    Funkcja wyższego rzędu, która analizuje listę dokumentów
    :param docs:
    :param analisys_fn:
    :return: zwraca informację o liczbie wystąpień każdego słowa we wszystkich dokmentach - globalnie
    """
    aggregate_counter = Counter()
    for doc in docs:
        result = analisys_fn(doc)
        aggregate_counter.update(result)
    return dict(aggregate_counter)

#przykładowa funkcja analizy
def word_frequency_analisys(text:str) -> Dict[str,int]:
    """
    funkcja analizy tekstu dokumentu
    :param text:
    :return: częstotliwosc wystąpien słów dłuższych niż 3 znaki pomojając stopwords
    """
    stopwords = {'the','and','this','that','with','from','which'}
    words = re.findall(r'\b\w+\b',text.lower())
    filtered_words = [w for w in words if len(w)>3 and w not in stopwords]
    return dict(Counter(filtered_words))

def keyword_sentence_count(text:str,keyword:str="text")->Dict[str,int]:
    """
    funkcja liczy ile zdań w tekściezawiera wskazane słowo kluczowe
    :param text:
    :param keyword:
    :return: słownik z liczbą zdań zawierających słowo kluczowe
    """
    sentences = re.split(f'[.!?]',text)
    count = sum(1 for sentence in sentences if keyword.lower() in sentence.lower())
    return {keyword:count}

documents = [
    "This is a sample document with some sample text and additional sample data. Big text",
    "Another document, which contains different text and information from the first one.",
    "Text mining and natural language processing are interesting fields. My text"
]

result = process_documents(documents,word_frequency_analisys)
print(result)

print("_"*60)

analisys_with_keyword = partial(keyword_sentence_count,keyword="text")
keyword_result = process_documents(documents,analisys_with_keyword)
print(keyword_result)
