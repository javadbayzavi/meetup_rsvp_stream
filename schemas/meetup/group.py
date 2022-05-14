import json
from lib.models.model import model

class group(model):
    def __init__(self,propertyList,topicList = None) -> None:
        super().__init__(propertyList["group_id"])
        if "group_name" in propertyList and propertyList["group_name"] != None:
            self.group_name = propertyList["group_name"]
        if "group_city" in propertyList and propertyList["group_city"] != None:
            self.group_city = propertyList["group_city"]
        if "group_country" in propertyList and propertyList["group_country"] != None:
            self.group_country = propertyList["group_country"]
        if "group_lon" in propertyList and propertyList["group_lon"] != None:
            self.group_lon = propertyList["group_lon"]
        if "group_lat" in propertyList and propertyList["group_lat"] != None:
            self.group_lat = propertyList["group_lat"]
        if "group_urlname" in propertyList and propertyList["group_urlname"] != None:
            self.urlname = propertyList["group_urlname"]
        if "group_state" in propertyList and propertyList["group_state"] != None:
            self.group_state = propertyList["group_state"]
        if  topicList != None and len(topicList) != None:
            self.group_topics = topicList
            
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)