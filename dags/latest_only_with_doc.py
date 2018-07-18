#dags/latest_only_with_trigger.py
import datetime as dt

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator
from airflow.utils.trigger_rule import TriggerRule


dag = DAG(
    dag_id='latest_only_with_trigger_with_doc',
    schedule_interval=dt.timedelta(hours=1),
    start_date=dt.datetime(2018, 6, 25),
)

dag.doc = "Hello Tony, what can I do for you?"
dag.doc_md = __doc__

latest_only = LatestOnlyOperator(task_id='latest_only', dag=dag)

task1 = DummyOperator(task_id='task1', dag=dag)
task1.set_upstream(latest_only)

task2 = DummyOperator(task_id='task2', dag=dag)

task3 = DummyOperator(task_id='task3', dag=dag)
task3.set_upstream([task1, task2])

task4 = DummyOperator(task_id='task4', dag=dag,
                      trigger_rule=TriggerRule.ALL_DONE)
task4.set_upstream([task1, task2])


latest_only.doc_md = """\
#NewTitle
Here's a [url](www.airbnb.com)
"""

latest_only.doc = "I am Ray "