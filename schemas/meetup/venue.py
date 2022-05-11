from lib.models import model
class venue(model):
    def __init__(self,id,name,lon,lat) -> None:
        super().__init__(id)
        self._venue_name = name
        self._long = lon
        self._lat = lat
        