import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


## get command line arguments and take 2nd , 3rd, 4th, to the end. 
## if no argument provided, hello world will be used instead
message = ' '.join(sys.argv[1:]) or "Hello World from send_task!"


## get command line arguments and take 2nd , 3rd, 4th, to the end. 

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(" [x] Sent %r", message)