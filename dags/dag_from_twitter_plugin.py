from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import TwitterTimelineSensor
from airflow.operators import TwitterTimelineOperator

dag = DAG('dag_for_twitter_plugin', description='Twitter Plugin DAG',
          schedule_interval='0 * * * *',
          start_date=datetime(2018, 6, 25), catchup=False)

dummy_task = DummyOperator(task_id='dummy_task', dag=dag)

twitter_timeline_sensor_task = TwitterTimelineSensor(task_id='twitter_timeline_sensor', poke_interval=60, dag=dag)

twitter_timeline_operator_task = TwitterTimelineOperator(my_operator_param='This is a test.',
                                task_id='twitter_timeline_operator', dag=dag)
                                

dummy_task >> twitter_timeline_sensor_task >> twitter_timeline_operator_task