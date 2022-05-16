import json
from lib.core.server import server
from lib.utils.config import config
from workers.worker import worker
from lib.core.db import dbEngine


class publisher(worker):
    def __init__(self, name,  broker) -> None:
        super().__init__(name, broker)
    
    def processMe(self):
        try:
            if server.brokerChecking(config.PUBLISHER_TOPIC) == False:
                server.brokerConfigReset()

            #Subscribe consumer to topic
            self.brokerCLient.subscribe([config.PUBLISHER_TOPIC])

            #pull recent message from topic
            data = self.pullStream()

            #dump new result into Db for client resolution
            self.dumpDb(data.pop())
        
            self.updateActionList("processed") 
        except Exception as ex:
            self.updateActionList(" exception catched. caused by:" + str(ex))
            self._unhealthyrun += 1
            pass


    def dumpDb(self, data):
        if data == None:
            return

        db_persist = dbEngine()
        
        #Referesh result set
        refresh_stmt = "Delete from city_trend"
        db_persist.exeuteQuery(refresh_stmt,None)

        for res in data:
            stmt = "Insert into city_trend (name,lon,lat,point) VALUES (%s,%s,%s,%s)"
            params = (res["name"],res["lon"],res["lat"],res["point"])
            db_persist.exeuteQuery(stmt,params)

        self.updateActionList("result dumped to DB") 
    
    def pullStream(self) -> any:
        data = []
        for message in self.brokerCLient:
            jdata = json.loads(message.value)
            data.append(jdata)
        
        self.updateActionList("stream pulled") 
        return data
