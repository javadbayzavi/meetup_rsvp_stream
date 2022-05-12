from lib.models.model import model

class venue(model):
    def __init__(self,propertyList) -> None:
        super().__init__(propertyList["venue_id"])
        if "venue_name" in propertyList and propertyList["venue_name"] != None:
            self._venue_name = propertyList["venue_name"]
        if "lon" in propertyList and propertyList["lon"] != None:
            self._lon = propertyList["lon"]
        if "lat" in propertyList and propertyList["lat"] != None:
            self._lat = propertyList["lat"]            
