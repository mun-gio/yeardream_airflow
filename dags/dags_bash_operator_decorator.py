from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

@DAG(
    dag_id="dags_bash_operator_decorator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    catchup=True,
    tags=["homework"],
)
def my_dag():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    my_dag(bash_t1) >> my_dag(bash_t2)