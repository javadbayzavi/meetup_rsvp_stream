from lib.models import model

class event(model):
    def __init__(self,id,name,time,url) -> None:
        super().__init__(id)
        self._event_name = name
        self._time = time
        self._event_url = url
        
