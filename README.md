conectarse :

docker exec -it kafka-broker bash

Crear topic 

kafka-topics --bootstrap-server kafka-broker:9092 --create --topic eventos


Productor:
kafka-console-producer --broker-list kafka-broker:9092 --topic eventos


consumidor: 
kafka-console-consumer --bootstrap-server kafka-broker:9092 --topic eventos --from-beginning


https://github.com/ktechhub/deploy_kafka_docker/blob/main/consumer.py