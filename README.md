This project allows understanding the basic configuration of a Docker container, which will run an Apache Kafka broker receiving messages from a Python producer with random data. All messages received by Kafka will be collected by a Python consumer, which will then insert them into a MongoDB NoSQL database. The stored data can be visualized using Mongo Express from a web browser by accessing the host URL and port 8081.


# Kafka :

docker exec -it kafka-broker bash

Create topic 

kafka-topics --bootstrap-server kafka-broker:9092 --create --topic eventos


Producer:
kafka-console-producer --broker-list kafka-broker:9092 --topic eventos


Consumer: 
kafka-console-consumer --bootstrap-server kafka-broker:9092 --topic eventos --from-beginning

Note: Automatically, the topic associated with the name assigned to the environment variable TOPIC will be created. This ensures the existence of a topic so that the producer can send messages without any issues


# DATA BASE
The database is a MongoDB. Upon container creation, the init-mongo file will be executed to create the database named 'logs' and the collection named 'events'