import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def print_start():
    print('========starting========')

def print_end():
    print('========ending========')


default_args = {
    'owner': 'tonylin1000',
    'start_date': dt.datetime(2018, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}


with DAG('jinja_task_1',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    print_start = PythonOperator(task_id='print_start',
                                 python_callable=print_start)                                                              

    print_end = PythonOperator(task_id='print_end',
                                 python_callable=print_end)                               

    templated_command = """
    {% for i in range(2) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7) }}"
        echo "Hi {{ params.name  }} {{ i }}"
        echo "{{ params.name ~ params.complement  }} "
    {% endfor %}
    """
    
    jinja_task = BashOperator(
        task_id='my_jinja_template',
        bash_command=templated_command,
        params={'complement': ' is a handsome boy.', 
                'name': 'Tony'},
        dag=dag)


print_start >> jinja_task >> print_end 