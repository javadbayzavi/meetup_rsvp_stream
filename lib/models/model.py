from abc import ABC
from random import randint



class model(dict):
# class model(ABC):
    def __init__(self,id="") -> None:
        self.id = id
        
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self , value) -> None:
        if value != None and value != "":
            self._id = value
        else:
            self._id = str(randint(0,10000))
