from lib.models.model import model

class event(model):
    def __init__(self,propertyList) -> None:
        super().__init__(propertyList["event_id"])
        if "event_name" in propertyList and propertyList["event_name"] != None:
            self._event_name = propertyList["event_name"]
        if "time" in propertyList and propertyList["time"] != None:
            self._time = propertyList["time"]
        if "event_url" in propertyList and propertyList["event_url"] != None:
            self._event_url = propertyList["event_url"]
        
