from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mongodb_dag',
    default_args=default_args,
    schedule_interval='@once'
)

def create_database():
    # MongoDB connection parameters
    connection_string = "mongodb+srv://sparkydz:sparkydz@cluster0.vpich6m.mongodb.net/"
    database_name = "db"
    
    try:
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        # Create a new database
        database = client[database_name]
        
        # Create collections (tables) and insert example data
        collection1 = database["collection1"]
        collection1.insert_one({"name": "Example 1"})
        
        collection2 = database["collection2"]
        collection2.insert_one({"name": "Example 2"})
        
        print("Database created successfully!")
        
    except PyMongoError as e:
        print("Error connecting to MongoDB:", e)

create_database_task = PythonOperator(
    task_id='create_database',
    python_callable=create_database,
    dag=dag
)

create_database_task
