import os
import subprocess
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

AIRFLOW_HOME = os.getenv("AIRFLOW_HOME", "/opt/airflow")


def run_ingestion_script():
    script_path = os.path.join(AIRFLOW_HOME, "src/ingestion/fetch_telemetry.py")
    subprocess.run(
        ["python", script_path],
        env={**os.environ, "PYTHONPATH": AIRFLOW_HOME},
        check=True,
    )


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2026, 9, 1),
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="aviation_telemetry_ingestion",
    default_args=default_args,
    description="Fetch real-time flight telemetry from OpenSky API",
    schedule="@hourly",
    catchup=False,
) as dag:

    fetch_telemetry_task = PythonOperator(
        task_id="fetch_telemetry_task",
        python_callable=run_ingestion_script,
    )