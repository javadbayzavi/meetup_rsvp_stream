from kafka import KafkaClient
from lib.utils.config import config
import requests
from workers.worker import worker
import json

class producer(worker):
    __producer = None

    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #load Raw Data from stream
        data = self.loadJoson()

        #push the stream into Kafka Broker
        self.pushStream(data)

    #TODO: Develop Aysnc method for producer
    def processMeAsync(self):
            data = self.loadJoson()
            print(data)
        #production starts from here
        

    #TODO: Connect operation must be expanded
    def connect(self) -> bool:
        return True
    

    #TODO: Disconnect operation must be expanded
    def disconnect(self) -> bool:
        return True


    #Push entry message into kafka broker
    def pushStream(self , strem):
        client = KafkaClient(hosts = config.BROKER_PATH)
        topic = client.topics["test"]
        content = json.dumps(strem , indent=4)

        with topic.get_sync_producer() as producer:
            encoded_message = content.encode("utf-8")
            producer.produce(encoded_message)


    #Load json stream from meetup RSVP
    def loadJoson(self) -> any:
        #TODO: Fetch data from meetup RSVP
        req  = requests.get(config.MEETUP_RSVP_ENDPOINT)
        data = req.json()
        return data