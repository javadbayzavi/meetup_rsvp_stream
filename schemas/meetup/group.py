from lib.models.model import model

class group(model):
    def __init__(self,propertyList,topicList) -> None:
        super().__init__(propertyList["group_id"])
        if "group_name" in propertyList and propertyList["group_name"] != None:
            self._group_name = propertyList["group_name"]
        if "group_city" in propertyList and propertyList["group_city"] != None:
            self._group_city = propertyList["group_city"]
        if "group_country" in propertyList and propertyList["group_country"] != None:
            self._group_country = propertyList["group_country"]
        if "group_lon" in propertyList and propertyList["group_lon"] != None:
            self._group_lon = propertyList["group_lon"]
        if "group_lat" in propertyList and propertyList["group_lat"] != None:
            self._group_lat = propertyList["group_lat"]
        if "group_urlname" in propertyList and propertyList["group_urlname"] != None:
            self._urlname = propertyList["group_urlname"]
        if "group_state" in propertyList and propertyList["group_state"] != None:
            self._group_state = propertyList["group_state"]
        if len(topicList) != None:
            self._group_topics = topicList
            