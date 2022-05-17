

from datetime import datetime
from lib.core.webserver import serverManager
from workers.worker import  workerInterface


class schedulerEngine():
    __threadpool = {}
    __threadProfile = {}
    def __init__(self) -> None:
        web = serverManager()
        web.start()

    def schedule(self,thread : workerInterface, sleep = 5):
        thread.sleep = sleep
        self.__threadpool[thread.broker] = thread
        self.__threadProfile[thread.broker] = []
        self.engineProfiling(thread.broker, thread.broker + ": Scheduled at " + str(datetime.now()))
    
    def startManually(self,t_name):
        thread = self.__threadpool[t_name]
        thread.observer = self
        thread.run()

    def getProcessPoolCount(self) -> int:
        return (len(self.__threadpool))

    def getProcessProfileCount(self) -> int:
        return (len(self.__threadProfile))

    #Simply profiling the last status of the engine part
    def engineProfiling(self,enginePart, status):
        engineprofile = self.__threadProfile[enginePart]
        engineprofile.append(status)

    def safeTerminate(self,enginePart:workerInterface):
        self.engineProfiling(enginePart.broker, ": is saftely killed at" + str(datetime.now()))
        enginePart.join()
        del self.__threadpool[enginePart.broker]
        del self.__threadProfile[enginePart.broker]

    def engineStart(self):

        #start all threads in threadpool
        for t in self.__threadpool:
            self.__threadpool[t].observer = self
            self.__threadpool[t].start()
            self.engineProfiling(t, t + ": Started at " + str(datetime.now()))

        while True:
            action = input("Select action to profile checking:")
            match action:
                case '1':
                    for s in self.__threadProfile['producerName']:
                        print(s)
                    pass
                case '2':
                    for s in self.__threadProfile['consumerName']:
                        print(s)
                    pass
                case '3':
                    for s in self.__threadProfile['analyzerName']:
                        print(s)
                    pass
                case '4':
                    for s in self.__threadProfile['publisherName']:
                        print(s)
                    pass
                case '5':
                    for t in self.__threadpool:
                        try:
                            self.__threadpool[t].join()
                        except Exception:
                            pass



