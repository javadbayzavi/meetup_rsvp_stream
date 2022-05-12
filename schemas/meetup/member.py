from lib.models.model import model

class member(model):
    def __init__(self,propertyList) -> None:
         super().__init__(propertyList["member_id"])
         if "member_name" in propertyList and propertyList["member_name"] != None:
            self._member_name =  propertyList["member_name"]
         if "photo" in propertyList and propertyList["photo"] != None:
            self._photo = propertyList["photo"]
        