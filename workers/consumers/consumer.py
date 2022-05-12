import json
from workers.worker import worker
from kafka import KafkaConsumer
from schemas.meetup.rsvp import rsvp
from schemas.meetup.venue import venue
from schemas.meetup.event import event
from schemas.meetup.member import member
from schemas.meetup.group import group
from schemas.meetup.grouptopic import grouptopic

class consumer(worker):
    def __init__(self, broker) -> None:
        #TODO: some string checking before set broker config
        self.broker = broker
    
    def processMe(self):

        data = self.pullStream()
        #Extract venue object
        m_venue = venue(data["venue"])

        #Extract member object
        m_member = member(data["member"])

        #Extract event object
        m_event = event(data["event"])

        #Extract group topic object
        m_groupTopics = []
        topicList = data["group"]["group_topics"]
        for topic in topicList:
            m_groupTopics.append(grouptopic(topic))

        #Extract group object
        m_group = group(data["group"],m_groupTopics)


        #Extract rsvp object
        m_rsvp = rsvp(data["rsvp_id"],data["visibility"],["response"],["guests"],data["mtime"],m_event,m_group,m_venue,m_member)


    def processMeAsync(self):
            data = self.pullStream()
            print(data)
        #production starts from here
        

    #TODO: Connect operation must be expanded
    def connect(self) -> bool:
        return True
    

    #TODO: Disconnect operation must be expanded
    def disconnect(self) -> bool:
        return True


    def pullStream(self) -> any:
        data = None
        #TODO: pull message from Kafka Broker
        with open('test.json', 'r', encoding="utf8") as f:
            data = json.load(f)
        return data