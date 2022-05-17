from lib.core.schedulerEngine import schedulerEngine
from lib.core.server import server
from lib.utils.config import config
from workers.factory import WorkerFactory


def main():

    #Broker configuration
    server.brokerConfigReset()
    
    #Initiate DB
    server.dbServerConfig()
    
    #1. Initiate producer engine part
    producer = WorkerFactory.createWorker(workerType = config.PRODUCER_KEY)

    #2. Initiate consumer engine part
    consumer = WorkerFactory.createWorker(workerType = config.CONSUMER_KEY)

    #3. Initiate publisher engine part
    publisher = WorkerFactory.createWorker(workerType = config.PUBLISHER_KEY)

    #4. Initiate subscriber engine part
    analyzer = WorkerFactory.createWorker(workerType = config.ANALYZER_KEY)



    #schedule all the app engine part for mutually run
    appEngine = schedulerEngine()
    appEngine.schedule(producer)
    appEngine.schedule(consumer)
    appEngine.schedule(publisher)
    appEngine.schedule(analyzer)

    #Start the app engine
    appEngine.engineStart()

    #appEngine.startManually(producer.broker)
    #appEngine.startManually(consumer.broker)
    #appEngine.startManually(analyzer.broker)
    #appEngine.startManually(publisher.broker)
        

if __name__ == "__main__":
    main()