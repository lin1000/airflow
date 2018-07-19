
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

def bbs_beauty(**kwargs):
    print(str(kwargs))
    execution_date = kwargs['execution_date']
    crawl_bbs_beauty.operator_trigger(execution_date)
    print("execution_date="+ str(execution_date))
    print("execution_date="+ str(type(execution_date)))
    xcom_return = {}
    xcom_return.update({'execution_date':execution_date})
    return xcom_return

def bbs_tennis(**kwargs):
    print(str(kwargs))
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



bbs_beauty_op = PythonOperator(task_id='bbs_beauty',
                                provide_context=True,
                                python_callable=bbs_beauty,
                                dag=dag)

bbs_tennis_op = PythonOperator(task_id='bbs_tennis',
                                provide_context=True,
                                python_callable=bbs_tennis,
                                dag=dag)                                 
dummy_operator = DummyOperator(
  task_id='www.ptt.cc_task',
  dag=dag,
)

dummy_operator.set_upstream(bbs_beauty_op)
dummy_operator.set_upstream(bbs_tennis_op)