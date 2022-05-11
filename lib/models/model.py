from abc import ABC



class model(ABC):
    def __init__(self,id) -> None:
        self.id = id
        
    @property
    def id(self) -> str:
        return self._id
    
    @property.setter
    def id(self , value) -> None:
        self._id = value
