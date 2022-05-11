from lib.models import model

class member(model):
    def __init__(self,id,name,photo,lat) -> None:
        super().__init__(id)
        self._member_name = name
        self._photo = photo
        