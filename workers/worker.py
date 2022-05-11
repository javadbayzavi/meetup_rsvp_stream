
from abc import ABC, abstractmethod


class workerInterface(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def processMe(self):
        pass


class worker(workerInterface):
    @property
    def broker(self) -> str:
        return self._broker
    
    @property.setter
    def broker(self,address) -> None:
        self._broker = address
    
    # Strategy Pattern, initiate for DI
    def run(self):
        self.processMe()
