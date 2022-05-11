import lib.models as model
class group(model):
    def __init__(self,id,name,city,country,lon,lat,url) -> None:
        super().__init__(id)
        self._group_name = name
        self._group_city = city
        self._group_country = country
        self._group_lon = lon
        self._group_lat = lat
        self._urlname = url
        #TODO: initiate the group moel at initiator