import airflow
from builtins import range
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG('myDag', default_args=args,
            schedule_interval="0 0 * * *",
            dagrun_timeout=timedelta(minutes=60))

cmd = "ping www.lin1000.com"

run_this_last = DummyOperator(task_id="run_this_last", dag=dag)

run_this = BashOperator(task_id="run_after_loop", bash_command="echo 1",dag=dag)
run_this.set_downstream(run_this_last)

for i in range(3):
    i = str(i)
    task = BashOperator(task_id="runme_"+i,bash_command='echo {{ task_instance_key_str }} && sleep 1', dag=dag)
    task.set_downstream(run_this)


task = BashOperator(task_id="also_run_this_2",
                    bash_command='echo "run_id ={{ run_id }} | dag_run={{ dag_run }}"',
                    dag=dag)
task.set_downstream(run_this_last)