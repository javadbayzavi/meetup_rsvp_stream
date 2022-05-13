from genericpath import exists
import time
from lib.core.server import server
from lib.utils.config import config
from workers.worker import worker
from kafka import KafkaConsumer, KafkaProducer
from schemas.meetup.rsvp import rsvp
from schemas.meetup.venue import venue
from schemas.meetup.event import event
from schemas.meetup.member import member
from schemas.meetup.group import group
from schemas.meetup.grouptopic import grouptopic
from lib.core.analyze import analyzer
import pandas as pd
import json


class consumer(worker):
    __consumer = None
    __publisher = None    
    def __init__(self, broker) -> None:
        super().__init__()
        self.broker = broker
        self.daemon = True
        self.__consumer = KafkaConsumer(bootstrap_servers = config.BROKER_PATH,
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        consumer_timeout_ms = 4000,
                                        )
        self.__publisher = KafkaProducer(bootstrap_servers = config.BROKER_PATH,
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))  
    
    def processMe(self):
        #Check for live connection to broker
        if self.connect() == False:
            return

        if server.brokerChecking(config.PRODUCER_TOPIC) == False:
            server.brokerConfigReset()

        #Subscribe consumer to topic
        self.__consumer.subscribe([config.PRODUCER_TOPIC])

        #pull recent message from topic
        data = self.pullStream()

        #extract pulled message into business objects(meetup entites)
        rsvpmessages = self.extractMessage(data)

        #dump extracted object to disk for aggregation
        #self.dumpToDisk(rsvpmessages)

        #Save the result to persist_data
        if server.brokerChecking(config.PUBLISHER_TOPIC) == False:
            server.brokerConfigReset()
        
        self.pushResult()
        
        self.__publisher.flush()

    def dumpToDisk(self,new_data, filename='data.json'):
        if exists(filename) == False:
            file = open(filename,"w")
            json.dump(json.dumps(new_data), file, indent = 4)

        else:
            with open(filename,'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data.append(x for x in new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
    
    def dumpToCloud(self,data):
        pass

    def extractMessage(self,data) -> any:
        res = []
        for rsItem in data:
            #Extract venue object
            m_venue = venue(rsItem["venue"])

            #Extract member object
            m_member = member(rsItem["member"])

            #Extract event object
            m_event = event(rsItem["event"])

            #Extract group topic object
            m_groupTopics = []
            topicList = rsItem["group"]["group_topics"]
            for topic in topicList:
                m_groupTopics.append(grouptopic(topic))

            #Extract group object
            m_group = group(rsItem["group"],m_groupTopics)


            #Extract rsvp object
            m_rsvp = rsvp(rsItem["rsvp_id"],rsItem["visibility"],["response"],["guests"],rsItem["mtime"],m_event,m_group,m_venue,m_member)
            res.append(m_rsvp)

        return res

    def processMeAsync(self):
            data = self.pullStream()
            print(data)
        #production starts from here
        

    def connect(self) -> bool:
        return self.__consumer.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.__consumer.close()
        return self.__consumer.bootstrap_connected()


    def pullStream(self) -> any:
        data = []
        for message in self.__consumer:
            jdata = json.loads(message.value)
            data.append(jdata)
        
        return data
        
    def pushResult(self) -> any:
        data = []
        for i in range(10):
            jdata = {
                "name":"name" + str(i),
                "lon" : str(2 * i + 12 * 1.5),
                "lat" : str(2 + i * 12 * 1.5),
                "point" : i
                    }
            data.append(jdata)

        self.__publisher.send(config.PUBLISHER_TOPIC, data)
        time.sleep(1)        
