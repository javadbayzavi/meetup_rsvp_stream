
from abc import ABC, abstractmethod
from threading import Thread
import time


class workerInterface(ABC,Thread):
    daemon: bool

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
    
    @broker.setter
    def broker(self,address) -> None:
        self._broker = address
    
    #TODO: develop process method to work on sleep and timer for process on/off switching
    def run(self) -> None:
        self.processMe()

    
    def processMe(self):
        pass
