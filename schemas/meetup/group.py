import lib.models as model
class group(model):
    def __init__(self,id,name,city,country,lon,lat,url,state) -> None:
        super().__init__(id)
        self._group_name = name
        self._group_city = city
        self._group_country = country
        self._group_lon = lon
        self._group_lat = lat
        self._urlname = url
        self._group_state = state
        self._group_topics = []
        #TODO: initiate the group moel at initiator