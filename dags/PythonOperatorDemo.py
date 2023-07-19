from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define the Python function to be executed by the PythonOperator
def print_message():
    print("Hello, this is a custom Airflow Python Operator!")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 18),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG object
dag = DAG(
    'example_python_operator',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Set the interval as per your requirement
)

# Create the PythonOperator and specify the task to execute the 'print_message' function
print_message_task = PythonOperator(
    task_id='print_message_task',
    python_callable=print_message,
    dag=dag,
)

# Define the task dependencies (if any)
# For this example, we don't have any dependencies
print_message_task

