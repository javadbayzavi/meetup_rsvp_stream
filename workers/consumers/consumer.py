from genericpath import exists
import os
import time

from pyparsing import line
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

import json


class consumer(worker):
    __consumer = None
    def __init__(self, broker) -> None:
        super().__init__()
        self.broker = broker
        self.daemon = True
        self.__consumer = KafkaConsumer(bootstrap_servers = config.BROKER_PATH,
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        group_id = "main",
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
        
        if data != None and len(data) > 0:
            #extract pulled message into business objects(meetup entites)
            rsvpmessages = self.extractMessage(data)

            #dump extracted object to disk for aggregation
            self.dumpToDisk(rsvpmessages)

    def dumpToDisk(self,new_data, filename='data.json'):
        if new_data == None or len(new_data) <= 0:
            return

        if exists(filename) == False:
            file = open(filename,"w")
            file.writelines(new_data)
        else:
            with open(filename,'r+') as file:
                file_data = []
                if os.path.getsize(filename) > 0:
                    # First we load existing data into a dict.
                    file_data = file.readlines()
                # Join new_data with file_data inside emp_details
                for item in new_data:
                    file_data.append(item)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                file.truncate()
                file.writelines(file_data)
    
    def dumpToCloud(self,data):
        pass

    def extractMessage(self,data) -> any:
        res = []
        for rsItem in data:
            #Extract venue object
            #m_venue = None
            #if "venue" in rsItem:
            #    m_venue = venue(rsItem["venue"])


            #Extract member object
            #m_member = None
            #if "member" in rsItem:
            #    m_member = member(rsItem["member"])

            #Extract event object
            #m_event = None
            #if "event" in rsItem:
            #    m_event = event(rsItem["event"])

            #Extract group topic object
            #m_groupTopics = []
            #if "group" in rsItem and "group_topics" in rsItem["group"]:
            #    topicList = rsItem["group"]["group_topics"]
            #    for topic in topicList:
            #        m_groupTopics.append(grouptopic(topic))

            # #Extract group object
            # m_group = None
            # if "group" in rsItem:
            #     # m_group = group(rsItem["group"],m_groupTopics)
            #     m_group = group(rsItem["group"],None)


            #Extract rsvp object
            m_rsvp = rsvp(rsItem["rsvp_id"],rsItem["visibility"],["response"],["guests"],rsItem["mtime"],rsItem["group"])
            # m_rsvp = rsvp(rsItem["rsvp_id"],rsItem["visibility"],["response"],["guests"],rsItem["mtime"],m_event,m_group,m_venue,m_member)
            res.append(json.dumps(m_rsvp) + '\n')

        return res

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
        