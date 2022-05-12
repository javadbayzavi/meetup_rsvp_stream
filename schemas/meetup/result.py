from lib.models.model import model

class result(model):
    def __init__(self,propertyList) -> None:
        super().__init__(propertyList["result_id"])
        if "city_name" in propertyList and propertyList["city_name"] != None:
            self._city_name = propertyList["city_name"]
        if "lon" in propertyList and propertyList["lon"] != None:
            self._lon = propertyList["lon"]
        if "lat" in propertyList and propertyList["lat"] != None:
            self._lat = propertyList["lat"]
        if "trend" in propertyList and propertyList["trend"] != None:
            self._trend = propertyList["trend"]
        
