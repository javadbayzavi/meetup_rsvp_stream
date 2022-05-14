import json
import time
from lib.core.server import server
from lib.utils.config import config
from workers.worker import worker
from kafka import KafkaProducer
from lib.core.analyzeEngine import analyzerEngine
import pandas as pd

class analyzer(worker):
    __analyzer = None 
       
    def __init__(self, broker) -> None:
        super().__init__()
        self.broker = broker
        self.daemon = True
        self.__producer = KafkaProducer(bootstrap_servers = config.BROKER_PATH,
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))   

    def processMe(self):
        
        #Check for live connection to broker
        if self.connect() == False:
            return
        
        if server.brokerChecking(config.PUBLISHER_TOPIC) == False:
            server.brokerConfigReset()
        
        #Save the result to persist_data
        self.pushResult()
        

       
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

        self.__analyzer.send(config.PUBLISHER_TOPIC, data)
        self.__analyzer.flush()
        time.sleep(1)  

    def analyzeTrend(self, data):

    def loadFromDisk(self):
        data = []
        with open('meetup.json',mode="r+", encoding="utf8") as f:
            try:
                f.seek(0)
                lines = f.readlines()
                for line in lines:
                    data.append(json.loads(line))
            except Exception as error:
                pass
            finally:
                return data
 
        
    def loadFromCloud():
        pass
    
    def connect(self) -> bool:
        return self.__analyzer.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.__analyzer.close()
        return self.__analyzer.bootstrap_connected()

