

from lib.core.webserver import serverManager
from workers.worker import  workerInterface


class schedulerEngine():
    __threadpool = {}
    def __init__(self) -> None:
        web = serverManager()
        web.start()

    def schedule(self,thread : workerInterface, sleep = 10):
        thread.sleep = sleep
        self.__threadpool[thread.broker] = thread
    
    def startManually(self,t_name):
        thread = self.__threadpool[t_name]
        thread.run()

    def engineStart(self):

        #start all threads in threadpool
        for t in self.__threadpool:
            pass

        while True:
            action = input("Select action to profile checking:")
            match action:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                   for t in self.__threadpool:
                       pass



