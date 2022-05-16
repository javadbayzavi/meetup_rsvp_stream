import json
from lib.models.model import model

class rsvp(model):
    def __init__(self,id,visible,respo,gust,mtime,propertyList) -> None:
        super().__init__(id)
        self.visibility = visible
        self.response = respo
        self.guests = gust
        self.mtime = mtime
        #TODO: This entities must be initiated in a separate initiator
        #self._event = event
        #self.group = group
        #self._venue = group
        #self._member = member
        #self._venue = venue

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

        dict.__init__(self, id = self.id, visibility = self.visibility, response = self.response, guests = self.guests , 
            mtime = self.mtime, group_name = self.group_name, group_city = self.group_city, group_lat = self.group_lat,
            group_lon = self.group_lon, group_country = self.group_country)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)