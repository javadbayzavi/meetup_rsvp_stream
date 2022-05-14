import time
from kafka import  KafkaProducer
from lib.utils.config import config
from lib.core.server import server
from workers.worker import worker
import json
import requests

class producer(worker):
    __producer = None

    def __init__(self, broker) -> None:
        super().__init__()
        self.broker = broker
        self.daemon = True
        self.__producer = KafkaProducer(bootstrap_servers = config.BROKER_PATH,
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))   
                                        
    def processMe(self):
        if self.connect() == False:
            return

        if server.brokerChecking(config.PRODUCER_TOPIC) == False:
            server.brokerConfigReset()
            
        #load Raw Data from stream
        data = self.loadJson()
        #push the stream into Kafka Broker
        self.pushStream(data)


    def connect(self) -> bool:
        return self.__producer.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.__producer.close()
        return self.__producer.bootstrap_connected()


    #Push entry message into kafka broker
    def pushStream(self , strem):
        self.__producer.send(config.PRODUCER_TOPIC, strem)
        self.__producer.flush()
        time.sleep(1)        


    #Load json stream from meetup RSVP
    def loadJson(self) -> any:
        req  = requests.get(config.MEETUP_RSVP_ENDPOINT)
        data = req.json()
        return data
    
