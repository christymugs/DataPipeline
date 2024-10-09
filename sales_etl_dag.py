from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# Define default arguments
default_args = {
    'owner': 'Christy',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

# Define the ETL pipeline in a DAG
with DAG('sales_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    # Task 1: Extract data from CSV
    def extract():
        sales_data = pd.read_csv('/path/to/sales_data.csv')
        sales_data.to_csv('/path/to/temp_extracted_data.csv', index=False)

    # Task 2: Transform data
    def transform():
        data = pd.read_csv('/path/to/temp_extracted_data.csv')
        # Simple transformation: Fill missing values
        data = data.fillna(0)
        data.to_csv('/path/to/temp_transformed_data.csv', index=False)

    # Task 3: Load data into PostgreSQL
    def load():
        engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
        transformed_data = pd.read_csv('/path/to/temp_transformed_data.csv')
        transformed_data.to_sql('sales_data', engine, if_exists='replace', index=False)

    # Define the Airflow tasks
    extract_task = PythonOperator(task_id='extract_task', python_callable=extract)
    transform_task = PythonOperator(task_id='transform_task', python_callable=transform)
    load_task = PythonOperator(task_id='load_task', python_callable=load)

    # Set the task order
    extract_task >> transform_task >> load_task
