from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'example-topic'

for _ in range(10):
    producer.send(topic, b"Test message")

producer.flush()
