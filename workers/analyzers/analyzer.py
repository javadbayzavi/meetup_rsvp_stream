import json
from numpy import sort
from lib.core.analyzeEngine import analyzerEngine
from lib.core.server import server
from lib.utils.config import config
from workers.worker import worker
import pandas as pd

class analyzer(worker):
       
    def __init__(self, name, broker) -> None:
        super().__init__(name, broker)

    def processMe(self):
        try:
            if server.brokerChecking(config.PUBLISHER_TOPIC) == False:
                server.brokerConfigReset()
            
            #load extracted data from persist area
            data = self.loadFromDisk()
            
            #Do some basic analysis on trends
            res = self.analyzeTrend(data)

            #push the result to broker
            self.pushResult(res)

            self.updateActionList("processed") 

        except Exception as ex:
            self.updateActionList(" exception catched. caused by:" + str(ex))
            self._unhealthyrun += 1
            pass
       
    def pushResult(self , res) -> any:
        self.brokerCLient.send(config.PUBLISHER_TOPIC, res)
        self.brokerCLient.flush()
        self.updateActionList("stream pushed") 

    def analyzeTrend(self, data):
        dataAnalyzer = analyzerEngine()
        result = dataAnalyzer.analyzeTrend(data)

        self.updateActionList("stream analyzed") 

        result.sort(key =lambda e : e["point"], reverse=True)

        # if len(result) <= 60:
        #     return result
        # else:
        #     return result[:60]
        return result


    def loadFromDisk(self):
        data = []
        with open('data.json',mode="r", encoding="utf8") as f:
            try:
                f.seek(0)
                lines = f.readlines()
                for line in lines:
                    data.append(json.loads(line))
            except Exception as error:
                pass
            finally:
                self.updateActionList("loaded from disk") 
                return data
 
    #Load from MongoDB
    def loadFromCloud():
        pass
