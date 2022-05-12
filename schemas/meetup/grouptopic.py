from lib.models.model import model

class grouptopic(model):
    def __init__(self,propertyList) -> None:
        super().__init__()
        if "topic_name" in propertyList and propertyList["topic_name"] != None:
            self._topic_name = propertyList["topic_name"]
        if "urlkey" in propertyList and propertyList["urlkey"] != None:
            self._urlKey = propertyList["urlkey"]