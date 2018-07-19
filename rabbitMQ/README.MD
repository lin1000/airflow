# Package for Python Clients

```bash
pip install pika

# Send a Hello World Message (verified)
python basic/send.py

# Send a Message that represent a complex task with delay (verified)
python basic/send_task.py

# Receive Messages a with different options (verified)
python basic/receive.py
python basic/receive_task.py
python basic/receive_task_detail.py
python basic/receive_basic_ack.py
python basic/receive_no_ack.py

# Send a Message to durable_queue (verified)
python durable_queue/send_task_durable.py

# Receive Messages a with different options (verified)
python durable_queue/receive_task_basic_ack.py
python durable_queue/receive_task_basic_ack_basic_ops.py
```

# Docker Commands

```bash
docker pull rabbitmq:3-management
docker stop lin1000-rabbitmq 
docker start lin1000-rabbitmq 
docker run -d -p 5672:5672 -p 15672:15672  --name lin1000-rabbitmq rabbitmq:3-management
docker exec -it lin1000-rabbitmq /bin/bash
rabbitmqctl list_queues
```

* RabbitMQ Admin UI (guest / guest) [http://localhost:15672/]


