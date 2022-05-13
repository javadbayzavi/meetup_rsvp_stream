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
        #while True:
            #load Raw Data from stream
        data = self.loadJoson()
        #push the stream into Kafka Broker
        self.pushStream(data)

        self.__producer.flush()

    #TODO: Develop Aysnc method for producer
    def processMeAsync(self):
        data = self.loadJoson()
        
    def connect(self) -> bool:
        return self.__producer.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.__producer.close()
        return self.__producer.bootstrap_connected()


    #Push entry message into kafka broker
    def pushStream(self , strem):
        self.__producer.send(config.PRODUCER_TOPIC, strem)
        time.sleep(1)        


    #Load json stream from meetup RSVP
    def loadJoson(self) -> any:
        #TODO: Fetch data from meetup RSVP
        req  = requests.get(config.MEETUP_RSVP_ENDPOINT)
        data = req.json()
        return data