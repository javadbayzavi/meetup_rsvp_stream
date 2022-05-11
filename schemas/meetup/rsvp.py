from lib.models import model
class rsvp(model):
    def __init__(self,id,visible,respo,gust) -> None:
        super().__init__(id)
        self._visibility = visible
        self._response = respo
        self.guests = gust
        