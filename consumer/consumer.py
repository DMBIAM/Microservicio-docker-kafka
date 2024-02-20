from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import logging

# Configure logging level
logging.basicConfig(level=logging.ERROR)

# Kafka server configuration
kafka_server = ["kafka-broker:9093"]
topic = 'eventos'

try:

    # Kafka consumer configuration
    consumer = KafkaConsumer(
                             bootstrap_servers=kafka_server,
                             group_id='logs_consumer',
                             auto_offset_reset="latest",
                             value_deserializer=json.loads)
                             
    consumer.subscribe(topic)
    
    # Process Kafka messages
    for message in consumer:
        event = message.value
        try:
            print(f"Event: {event}")
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            logging.error("Error decoding JSON message: %s", e)
            continue
except Exception as e_kafka:
    logging.error("Error connecting to Kafka: %s", e_kafka)
