import pika
import sys
import time

def callback(ch, method, properties, body):
    print(" [x] Received",body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" [x] Ack sended")



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='durable_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='durable_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()                      

connection.close()