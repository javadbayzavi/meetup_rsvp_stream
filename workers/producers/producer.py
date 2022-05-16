from lib.utils.config import config
from lib.core.server import server
from workers.worker import worker
import requests

class producer(worker):

    def __init__(self, name, broker) -> None:
        super().__init__(name, broker)
                                        
    def processMe(self):
        try:
            if server.brokerChecking(config.PRODUCER_TOPIC) == False:
                server.brokerConfigReset()
                
            #load Raw Data from stream
            data = self.loadJson()
            #push the stream into Kafka Broker
            self.pushStream(data)

            #log purpose
            self.updateActionList("processed") 
        except Exception as ex:
            self.updateActionList(" exception catched. caused by:" + str(ex))
            self._unhealthyrun += 1
            pass

    #Push entry message into kafka broker
    def pushStream(self , strem):
        self.brokerCLient.send(config.PRODUCER_TOPIC, strem)
        self.brokerCLient.flush()
        self.updateActionList("Stream pushed") 


    #Load json stream from meetup RSVP
    def loadJson(self) -> any:
        req  = requests.get(config.MEETUP_RSVP_ENDPOINT)
        data = req.json()
        self.updateActionList("Stream loaded") 
        return data
    
