from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils import dates
from airflow.utils.helpers import chain


def default_options():
    default_args = {
        "owner": "airflow",  # 拥有者名称
        "start_date": dates.days_ago(1),  # 第一次开始执行的时间，为 UTC 时间
        "retries": 1,  # 失败重试次数
        "retry_delay": timedelta(seconds=5),  # 失败重试间隔
    }
    return default_args


# 定义DAG
def test1(dag):
    t = "pwd"
    # operator 支持多种类型， 这里使用 BashOperator
    task = BashOperator(
        # task_id  # 指定要执行的命令  # 指定归属的dag
        task_id="test1",
        bash_command=t,
        dag=dag,
    )
    return task


def hello_world_1():
    current_time = str(datetime.today())
    print("hello world at {}".format(current_time))


def test2(dag):
    # PythonOperator
    task = PythonOperator(
        task_id="test2", python_callable=hello_world_1, dag=dag  # 指定要执行的函数
    )
    return task


def test3(dag):
    t = "top"
    task = BashOperator(task_id="test3", bash_command=t, dag=dag)
    return task


with DAG(
    "test_task",  # dag_id
    default_args=default_options(),  # 指定默认参数
    schedule_interval="20 8 * * *",  # 执行周期
) as d:
    task1 = test1(d)
    task2 = test2(d)
    task3 = test3(d)
    chain(task1, task2, task3)  # 指定执行顺序
