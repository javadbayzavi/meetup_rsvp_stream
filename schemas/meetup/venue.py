from lib.models import model
class venue(model):
    def __init__(self,propertyList) -> None:
        super().__init__(propertyList["venue_id"])
        if propertyList["venue_name"] != None:
            self._venue_name = propertyList["venue_name"]
        if propertyList["lon"] != None:
            self._lon = propertyList["lon"]
        if propertyList["lat"] != None:
            self._lat = propertyList["lat"]            

    def __init__(self,id,name,lon,lat) -> None:
        super().__init__(id)
        self._venue_name = name
        self._long = lon
        self._lat = lat
        