from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import logging

# Configure logging level
logging.basicConfig(level=logging.ERROR)

# Kafka server configuration
kafka_server = ["kafka-broker:9093"]
topic = 'eventos'

# user and pwd of MongoDB, only use data into plaint text for local environment o test, never use into production enviroment
username = 'root'
password = 'password'


try:

    # Kafka consumer configuration
    consumer = KafkaConsumer(
                             bootstrap_servers=kafka_server,
                             group_id='logs_consumer',
                             auto_offset_reset="latest",
                             value_deserializer=json.loads)
                             
    consumer.subscribe(topic)

    try:
        # Connect to MongoDB
        mongo_client = MongoClient('mongodb', 27017, username=username, password=password)
        db = mongo_client['logs']
        eventos_collection = db['events']

            # Process Kafka messages
        for message in consumer:
            event = message.value
            try:
                try:
                    # Insert into MongoDB
                    eventos_collection.insert_one(event)
                    print(f"Event inserted into MongoDB: {event}")
                except Exception as e_mongo:
                    logging.error("Error inserting event into MongoDB: %s", e_mongo)
            except json.JSONDecodeError as e:
                # Handle JSON decoding error
                logging.error("Error decoding JSON message: %s", e)
                continue

    except Exception as e:   
        print("Unauthorized user to connect MongoDB:", e)
    

except Exception as e_kafka:
    logging.error("Error connecting to Kafka: %s", e_kafka)
