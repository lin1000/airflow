"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators import HttpSensor, SimpleHttpOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 7, 1),
    'email': ['lin1000@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'lin1000_domain_checker',
    default_args=default_args, 
    schedule_interval="* * * * *")

domain01_sensor = HttpSensor(
    task_id='lin1000_domain_sensor',
    endpoint='',
    http_conn_id='lin1000_domain_http',
    retries=1,
    params={},
    dag=dag)

dummy_operator = DummyOperator(
  task_id='dummy_task',
  dag=dag,
)

dummy_operator.set_upstream(domain01_sensor)