from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Use Linux-style path for WSL
sys.path.append("/home/sheela/airflow/dags/scripts")

# Importing Python functions from scripts
from data_pull_1 import pull_orders_sample
from data_pull_2 import pull_orders_complete
from clean_data import clean_and_merge
from load_data import load_to_postgres
from kpi_analysis import run_kpi_analysis

default_args = {
    'owner': 'sheela',
    'start_date': datetime(2025, 5, 1),
    'retries': 1,
}

with DAG(
    dag_id='orderinfo_etl_pipeline',
    default_args=default_args,
    schedule='@daily',  
    catchup=False,
    tags=['etl', 'postgres', 'kpi'],
) as dag:

    task_pull1 = PythonOperator(
        task_id='pull_orders_sample',
        python_callable=pull_orders_sample
    )

    task_pull2 = PythonOperator(
        task_id='pull_orders_complete',
        python_callable=pull_orders_complete
    )

    task_clean = PythonOperator(
        task_id='clean_data',
        python_callable=clean_and_merge
    )

    task_load = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres
    )
    
    task_kpi = PythonOperator(
    task_id='run_kpi_analysis',
    python_callable=run_kpi_analysis
    )

    [task_pull1, task_pull2] >> task_clean >> task_load >> task_kpi
