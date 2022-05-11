import lib.models as model
class grouptopic(model):
    def __init__(self,id,name,urlk) -> None:
        super().__init__(id)
        self._topic_name = name
        self._urlKey = urlk
        #TODO: initiate the group topic moel at initiator