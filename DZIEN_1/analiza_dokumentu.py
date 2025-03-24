"""
Funkcja wyższego rzędu -> process_documents()
funkcja przyjmuje listę dokumentów -> artykułów, postów, recenzji...
Następnie wykonuje dodatkową agregację wyników.
Złożonośc: O(N*M*f(M)), gdzie N - liczba dokumentów, M - średnia długośc dokumentu,
f(M) -> funkcja złożonej analizy
"""

from typing import List,Callable,Dict
from collections import Counter
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
