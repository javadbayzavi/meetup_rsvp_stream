from lib.models.model import model

class rsvp(model):
    def __init__(self,id,visible,respo,gust,mtime,event,group,venue,member) -> None:
        super().__init__(id)
        self._visibility = visible
        self._response = respo
        self._guests = gust
        self._mtime = mtime
        #TODO: This entities must be initiated in a separate initiator
        self._event = event
        self._group = group
        self._venue = group
        self._member = venue

        