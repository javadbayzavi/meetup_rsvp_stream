
from abc import ABC, abstractmethod
from datetime import datetime
import json
from threading import Thread
import time

from kafka import KafkaConsumer, KafkaProducer

import lib.core.schedulerEngine as schedulerEngine
from lib.utils.config import config


class workerInterface(ABC,Thread):
    daemon: bool
    _sleeptime = int
    _broker = ''
    _actions = ''
    _observer = None
    _unhealthyrun = 0
    _brokerClient = None
    
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def processMe(self):
        pass

    @property
    def sleep(self) -> int:
        return self._sleeptime

    @sleep.setter
    def sleep(self,sleep:int):
        self._sleeptime = sleep

    @property
    def observer(self) -> schedulerEngine:
        return self._observer

    @observer.setter
    def observer(self,value : schedulerEngine):
        self._observer = value

    @property
    def brokerCLient(self):
        return self._brokerClient
    
    @brokerCLient.setter
    def brokerCLient(self,value) -> None:
        self._brokerClient = value


class worker(workerInterface):
    def __init__(self, name, broker):
        super().__init__()
        self.daemon = True
        self.broker = name
        self.inflateBrokerCLient(broker)
        self.updateActionList("Initiated") 

    @property
    def broker(self) -> str:
        return self._broker
    
    @broker.setter
    def broker(self,address) -> None:
        self._broker = address

    @property
    def actions(self) -> str:
        return self._actions
    
    @actions.setter
    def actions(self,value) -> None:
        self._actions = value
        
    def run(self) -> None:
        self.updateActionList("process started")
        while True:
            self.processMe()
            time.sleep(self.sleep)
            if self._unhealthyrun > 5:
                self.updateActionList("process unhealthy issue")
                time.sleep(self._sleeptime)
                continue
            elif self._unhealthyrun > 10:
                self.updateActionList("process crashed")
                self.observer.safeTerminate(self)
                break
            self.observer.engineProfiling(self.broker, self.actions)
            #self.actions = ''

    def inflateBrokerCLient(self, broker):
        match broker:
            case config.PRODUCER_KEY :
                self.brokerCLient = KafkaProducer(bootstrap_servers = config.BROKER_PATH,
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
                pass
            case  config.CONSUMER_KEY:
                self.brokerCLient = KafkaConsumer(bootstrap_servers = config.BROKER_PATH,
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        group_id = "main",
                                        consumer_timeout_ms = 4000,
                                        )
                pass
            case config.ANALYZER_KEY:
                self.brokerCLient = KafkaProducer(bootstrap_servers = config.BROKER_PATH,
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8')) 
                pass
            case config.PUBLISHER_KEY:
                self.brokerCLient = KafkaConsumer(bootstrap_servers = config.BROKER_PATH,
                                        auto_offset_reset='earliest',
                                        enable_auto_commit=True,
                                        consumer_timeout_ms = 4000,
                                        )
                pass

    def updateActionList(self, action):
        self.actions += self.broker + ": " + action + " at " + str(datetime.now()) + "\n"

    def processMe(self):
        pass


    def connect(self) -> bool:
        return self.brokerCLient.bootstrap_connected()
    

    def disconnect(self) -> bool:
        self.brokerCLient.close()
        return self.brokerCLient.bootstrap_connected()
