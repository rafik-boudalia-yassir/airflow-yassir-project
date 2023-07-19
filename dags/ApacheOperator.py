from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Default arguments for the DAG
default_args = {
    'owner': 'yassir',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'ApacheOperator',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Set the schedule interval as per your requirement
)

# Define tasks/operators for the DAG

# Task 1: BashOperator that prints a message
task_1 = BashOperator(
    task_id='print_message',
    bash_command='echo "Hello, Airflow!"',
    dag=dag,
)

# Task 2: BashOperator that runs a custom script
task_2 = BashOperator(
    task_id='run_custom_script',
    bash_command='python /path/to/your_custom_script.py',
    dag=dag,
)

# Define the task dependencies
task_1 >> task_2
