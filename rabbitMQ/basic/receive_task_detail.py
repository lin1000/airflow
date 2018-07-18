import pika
import sys
import time

def callback(ch, method, properties, body):
    print(" ==== ch ===" )
    for attr in sorted(dir(ch)):
        print(attr)
    print(" ==== ch.connection ===" )
    for attr in sorted(dir(ch.connection)):
        print(attr)
    print(" ==== ch.connection.channel ===" )
    for attr in sorted(dir(ch.connection.channel)):
        print(attr)

    print(" [x] Received ch.channel_number " + str(ch.channel_number))
    print(" [x] Received ch.is_open " + str(ch.is_open))
    print(" [x] Received method " + str(method))
    print(" [x] Received method.delivery_tag " + str(method.delivery_tag))
    print(" [x] Received properties " + str(properties))
    print(" [x] Received body " + str(body))
    print(" [x] Received body type" + str(type(body)))
    time.sleep(body.count(b'.'))
    print(" [x] Done")



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()                      

connection.close()