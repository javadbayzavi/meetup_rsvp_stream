#TODO: the app start the processing workflow
#1. Initiate producer thread
#2. run the producer
from lib.utils.config import config
from workers.factory import WorkerFactory


def main():
    #1. Initiate producer
    producer = WorkerFactory.createWorker(workerType = config.PRODUCER_KEY)

    #1. Initiate consumer
    consumer = WorkerFactory.createWorker(workerType = config.CONSUMER_KEY)

    #1. Initiate publisher
    publisher = WorkerFactory.createWorker(workerType = config.PUBLISHER_KEY)

    #1. Initiate subscriber
    subscriber = WorkerFactory.createWorker(workerType = config.SUBSCRIBER_KEY)


    while 1:
        producer.run()
        consumer.run()
        publisher.run()
        subscriber.run()

        

if __name__ == "__main__":
    main()