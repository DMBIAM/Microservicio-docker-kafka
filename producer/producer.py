import json
from datetime import datetime
from time import sleep
from random import choice
from kafka import KafkaProducer

# List of Kafka servers
kafka_server = ["kafka-broker:9093"]

# Topic to which data will be sent
topic = "eventos"

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Random values for generating example data
random_values = [1, 2, 3, 4, 5, 6, 7]

try:
    # Infinite loop to continuously send data
    while True:
        # Select a random value from the list
        random_value = choice(random_values)
        
        # Create the message with random data and a timestamp
        data = {
            "test_data": {
                "random_value": random_value
            },
            "timestamp": str(datetime.now()),
            "value_status": "High" if random_value > 5 else "Low"
        }
        
        # Print the message for visualization in the console
        print(data)
        
        # Send the message to the specified topic in Kafka
        producer.send(topic, data)
        
        # Ensure the message is sent immediately
        producer.flush()
        
        # Wait for 3 seconds before sending the next message
        sleep(3)
except Exception as e:
    # Log any errors that occur during message sending
    logging.error("Error sending message to Kafka: %s", e)