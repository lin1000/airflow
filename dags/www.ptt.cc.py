
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
from jobs.www_ptt_cc import crawl_bbs_beauty
from jobs.www_ptt_cc import crawl_bbs_tennis
from airflow.operators.python_operator import PythonOperator

def bbs_beauty():
    crawl_bbs_beauty.operator_trigger()

def bbs_tennis():
    crawl_bbs_tennis.operator_trigger()

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
    'www.ptt.cc_crawler',
    default_args=default_args, 
    schedule_interval="10 * * * *")



bbs_beauty_op = PythonOperator(task_id='bbs_beauty',python_callable=bbs_beauty,dag=dag)

bbs_tennis_op = PythonOperator(task_id='bbs_tennis',python_callable=bbs_tennis,dag=dag)                                 
dummy_operator = DummyOperator(
  task_id='www.ptt.cc_task',
  dag=dag,
)

dummy_operator.set_upstream(bbs_beauty_op)
dummy_operator.set_upstream(bbs_tennis_op)