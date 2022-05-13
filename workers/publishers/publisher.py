import json
from lib.core.server import server
from lib.utils.config import config
from workers.worker import worker
from kafka import KafkaConsumer
from lib.core.db import dbEngine


class publisher(worker):
    __publisher = None
        
    def __init__(self, broker) -> None:
        super().__init__()
        self.broker = broker
        self.daemon = True
        self.__publisher = KafkaConsumer(bootstrap_servers = config.BROKER_PATH,
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        consumer_timeout_ms = 4000,
                                        )
    
    def processMe(self):
        if self.connect() == False:
            return

        if server.brokerChecking(config.PUBLISHER_TOPIC) == False:
            server.brokerConfigReset()

        #Subscribe consumer to topic
        self.__publisher.subscribe([config.PUBLISHER_TOPIC])

        #pull recent message from topic
        data = self.pullStream()

        #dump new result into Db for client resolution
        self.dumpDb(data.pop())

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
    

    def connect(self) -> bool:
        return self.__publisher.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.__publisher.close()
        return self.__publisher.bootstrap_connected()

   
    def processMeAsync(self):
        #production starts from here
        pass
           
    def pullStream(self) -> any:
        data = []
        for message in self.__publisher:
            jdata = json.loads(message.value)
            data.append(jdata)
        return data

    def pullStreamTemp(self) -> any:
        data = []
        for i in range(10):
            jdata = {
                "name":"name" + str(i),
                "lon" : str(2 * i + 12 * 1.5),
                "lat" : str(2 + i * 12 * 1.5),
                "point" : i
                    }
            data.append(jdata)
        return data