from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.pipeline import run


with DAG(
    dag_id="etl_api_postgres",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="run_pipeline",
        python_callable=run
    )