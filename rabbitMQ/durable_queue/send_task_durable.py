import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


## get command line arguments and take 2nd , 3rd, 4th, to the end. 
## if no argument provided, hello world will be used instead
message = ' '.join(sys.argv[1:]) or "Message Content from send_task_durable!"


## get command line arguments and take 2nd , 3rd, 4th, to the end. 

channel.basic_publish(exchange='',
                      routing_key='durable_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

print(" [x] Sent", message)