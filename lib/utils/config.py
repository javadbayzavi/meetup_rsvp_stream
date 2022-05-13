class config:
    #TODO: Initiate the default config for kafka server
    BROKER_PATH = "127.0.0.1:9092"
    PRODUCER_TOPIC = "raw_topic"
    PUBLISHER_TOPIC = "result_topic"
    PRODUCER_KEY = "producer"
    CONSUMER_KEY = "consumer"
    PUBLISHER_KEY = "publisher"
    SUBSCRIBER_KEY = "subscriber"
    DEFAULT_SWITCH_TIME = 10
    MEETUP_RSVP_ENDPOINT = "http://localhost:900/test.json"
    SERVER_CLIENTID = "meetup_rsvp"
    WEBSERVER_HOST = "127.0.0.1"
    WEBSERVER_PORT = 999

    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASS = ""
    MYSQL_DB = "cities"