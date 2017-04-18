from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

#print("asd")

i = 0
while True:

    producer.send('test', b'some_message_bytes')
    time.sleep(2)
    i += 1
    #print(i)
