import pika
import sys
import time

def callback(ch, method, properties, body):
    print(" [x] Received",body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" [x] Ack sended")


credentials = pika.PlainCredentials('ibm', 'ibm1234')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='130.198.90.185',credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='q.central.matrial', durable=True)

channel.basic_consume(callback,
                      queue='q.central.matrial')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()                      

connection.close()