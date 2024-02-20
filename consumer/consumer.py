from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import logging

# Configure logging level
logging.basicConfig(level=logging.ERROR)

# Kafka server configuration
bootstrap_servers = ["kafka-broker:9093"]
topic = 'events'

try:
    # Connect to MongoDB
    mongo_client = MongoClient('mongo', 27017)
    db = mongo_client['logs']
    eventos_collection = db['events']

    # Kafka consumer configuration
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_servers,
                             group_id='logs_consumer',
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    # Process Kafka messages
    for message in consumer:
        event = message.value
        try:
            # Insert into MongoDB
            eventos_collection.insert_one(event)
            print(f"Event inserted into MongoDB: {event}")
        except Exception as e_mongo:
            logging.error("Error inserting event into MongoDB: %s", e_mongo)

except Exception as e_kafka:
    logging.error("Error connecting to Kafka: %s", e_kafka)
