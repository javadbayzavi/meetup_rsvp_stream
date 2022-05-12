#TODO: the app start the processing workflow
#1. Initiate producer thread
#2. run the producer
from lib.utils.config import config
from workers.factory import WorkerFactory
#Workflow 
# 1. Initiate the producer
# 2. run the producer as a thread
# 3. connect to RSVP streaming server at meetup
# 4. fetch stream data in a infinte loop
# 5. do a lite parsing on the format of the input stream
# 6. publish the raw message to the kafka broker
# 7. initiate a consumer 
# 8. run the consumer as a thread 
# 9. pull the message from kafka broker
# 10. check the message and parse it
# 11. add it to a data frame
# 12. do some data anlysis on dataframe
# 13. push the result to the kafka broker
# 14. initiate the publisher 
# 15. run the publisher as thread
# 16. pull result from kafka broker 
# s

def main():
    #1. Initiate producer
    producer = WorkerFactory.createWorker(workerType = config.PRODUCER_KEY)

    #1. Initiate consumer
    #consumer = WorkerFactory.createWorker(workerType = config.CONSUMER_KEY)

    #1. Initiate publisher
    #publisher = WorkerFactory.createWorker(workerType = config.PUBLISHER_KEY)

    #1. Initiate subscriber
    #subscriber = WorkerFactory.createWorker(workerType = config.SUBSCRIBER_KEY)


    while 1:
        producer.run()
       # consumer.run()
       # publisher.run()
       # subscriber.run()

        

if __name__ == "__main__":
    main()