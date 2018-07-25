# Airflow + CeleryExecutor to schedule 

## Technology Component Used :
* Airflow 1.9.0 with CeleryExector
* PostgreSQL (Docker)
* RabbitMQ (Docker)
* MongoDB (Docker)


## Commands to Activate
```bash
docker-compose up -d
source activate activate xxx_py3
source setenv.sh
airflow scheduler
airflow webserver -p 8080
```

## realtime data pipeline for crawler
The goal of this repo is to design a scalable data pipeline to collect, aggregate, and analyze sensors data from persoanl device Linkit + mpu9250. 


## List of Features 
[x] TBD

## Update Your Own Twitter Key and Secret at plugins/twitter_plugin.py
```python
consumer_key = '<YOUR_CONSUMER_KEY>'
consumer_secret = '<YOUR_CONSUMER_SECRET>'
access_token = '<YOUR_ACCESS_TOKEN>'
access_token_secret = '<YOUR_CONSUMER_TOKEN_SECRET>'
```
