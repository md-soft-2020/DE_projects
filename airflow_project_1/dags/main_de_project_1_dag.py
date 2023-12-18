from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Importing files
import sys
sys.path.append('/Users/mady/Desktop/Data Engineering/Projects/data_eng_project_1/airflow_project_1/data')

from create_tables import *

#Scheduling
with DAG(
    dag_id= "first_pipeline",
    start_date= datetime(2023, 12, 18),
    schedule_interval= "@daily",
    catchup= False,

) as dag:
    
    task_1 = PythonOperator(
        task_id = "db_connection",
        python_callable= connection
    )

    # task_2 = PythonOperator(
    #     task_id = "test",
    #     python_callable= hello_test
    # )

# task_1 >> task_2
