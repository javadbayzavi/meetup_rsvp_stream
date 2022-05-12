from schemas.meetup.rsvp import rsvp
from schemas.meetup.venue import venue
from workers.worker import worker
#from kafka import KafkaProducer
import json

class producer(worker):
    __producer = None

    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #load Raw Data from stream
        data = self.loadJoson()

        #Extract venue object
        
        m_venue = venue(data["venue"])

        #Extract member object

        #Extract event object

        #Extract group object

        #Extract group topic object

        #Extract rsvp object

        
        print(m_venue)
        #production starts from here

    def pushStream(self, *data:rsvp):
        a = True

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


    def loadJoson(self) -> any:
        data = None
        with open('test.json', 'r', encoding="utf8") as f:
            data = json.load(f)
        return data