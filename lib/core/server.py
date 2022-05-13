from kafka.admin import KafkaAdminClient, NewTopic
from lib.utils.config import config

class server:
    #Unhealthy operation: Be careful on using this operation
    def brokerReset():
        kafka_manager = KafkaAdminClient(
            bootstrap_servers = config.BROKER_PATH, 
            client_id = config.SERVER_CLIENTID
        )
        if config.PRODUCER_TOPIC in kafka_manager.list_topics():
            kafka_manager.delete_topics([config.PRODUCER_TOPIC])

        if config.PUBLISHER_TOPIC in kafka_manager.list_topics():
            kafka_manager.delete_topics([config.PUBLISHER_TOPIC])


    #Config broker with the required topics
    @staticmethod
    def brokerConfigReset():
        kafka_manager = KafkaAdminClient(
            bootstrap_servers = config.BROKER_PATH, 
            client_id = config.SERVER_CLIENTID
        )

        topic_list = kafka_manager.list_topics()

        new_topic = []

        if config.PRODUCER_TOPIC not in topic_list:
            new_topic.append(NewTopic(name = config.PRODUCER_TOPIC, num_partitions = 1, replication_factor = 1))

        if config.PUBLISHER_TOPIC not in topic_list:
            new_topic.append(NewTopic(name = config.PUBLISHER_TOPIC, num_partitions = 1, replication_factor = 1))

        if len(new_topic) > 0: 
            kafka_manager.create_topics(new_topics=new_topic, validate_only=False)

    #server topics health ckeking
    def brokerChecking(topicname:str) -> bool:
        kafka_manager = KafkaAdminClient(
            bootstrap_servers = config.BROKER_PATH, 
            client_id = config.SERVER_CLIENTID
        )
        return topicname in kafka_manager.list_topics()
    


