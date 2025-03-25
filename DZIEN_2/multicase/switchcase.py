from collections import defaultdict
from typing import Callable,Iterable,Any

class SwitchCaseMulti:
    def __init__(self):
        self._cases = defaultdict(list)
        self._default = None

    def case(self,keys:Iterable,action:Callable):
        """Dodawanie akcji do jednego lub więcej kluczy"""
        if not isinstance(keys,Iterable) or isinstance(keys,str):
            keys = [keys]
        for key in keys:
            self._cases[key].append(action)
        return self
    
    def default(self,action:Callable):
        """Akcja domyślna"""
        self._default = action
        return self
    
    def execute(self,key:Any,*args,**kwargs):
        """wykonanie wszystkich pasujących akcji"""
        actions = self._cases.get(key,[])
        if not actions and self._default:
            return self._default(*args,**kwargs)
        
        results = []
        for action in actions:
            results.append(action(*args,**kwargs))
        return results
    
    
    
