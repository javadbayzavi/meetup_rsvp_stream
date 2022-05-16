from genericpath import exists
import os
from lib.core.server import server
from lib.utils.config import config
from schemas.meetup.rsvp import rsvp
from workers.worker import worker
import json


class consumer(worker):
    def __init__(self, name,  broker) -> None:
        super().__init__(name, broker)

    
    def processMe(self):
        try:
            if server.brokerChecking(config.PRODUCER_TOPIC) == False:
                server.brokerConfigReset()

            #Subscribe consumer to topic
            self.brokerCLient.subscribe([config.PRODUCER_TOPIC])
            #pull recent message from topic
            data = self.pullStream()
            
            if data != None and len(data) > 0:
                #extract pulled message into business objects(meetup entites)
                rsvpmessages = self.extractMessage(data)

                #dump extracted object to disk for aggregation
                self.dumpToDisk(rsvpmessages)

            self.updateActionList("processed")

        except Exception as ex:
            self.updateActionList(" exception catched. caused by:" + str(ex))
            self._unhealthyrun += 1
            pass


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

        self.updateActionList("Message dumped To Disk") 
    
    def dumpToCloud(self,data):
        pass

    def extractMessage(self,data) -> any:
        res = []
        for rsItem in data:
            #Extract rsvp object
            m_rsvp = rsvp(rsItem["rsvp_id"],rsItem["visibility"],["response"],["guests"],rsItem["mtime"],rsItem["group"])
            res.append(json.dumps(m_rsvp) + '\n')

        self.updateActionList("Message extracted") 
        return res

    def pullStream(self) -> any:
        data = []
        for message in self.brokerCLient:
            jdata = json.loads(message.value)
            data.append(jdata)

        self.updateActionList("stream pulled") 
        return data
        