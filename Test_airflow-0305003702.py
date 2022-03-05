from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "Test_airflow-0305003702",
}

dag = DAG(
    "Test_airflow-0305003702",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.6.0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


# Operator source: examples/pipelines/introduction-to-generic-pipelines/load_data.ipynb
op_1af79fd3_7724_4626_8c1e_625c7bda77f8 = KubernetesPodOperator(
    name="load_data",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio_nginx_1:9000 --cos-bucket airflow --cos-directory 'Test_airflow-0305003702' --cos-dependencies-archive 'load_data-1af79fd3-7724-4626-8c1e-625c7bda77f8.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/load_data.ipynb' "
    ],
    task_id="load_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "ust8898865!@",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Test_airflow-0305003702-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: examples/pipelines/introduction-to-generic-pipelines/Part 1 - Data Cleaning.ipynb
op_a052ac6d_bddc_4a7d_9007_518e0d077f22 = KubernetesPodOperator(
    name="Part_1___Data_Cleaning",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio_nginx_1:9000 --cos-bucket airflow --cos-directory 'Test_airflow-0305003702' --cos-dependencies-archive 'Part 1 - Data Cleaning-a052ac6d-bddc-4a7d-9007-518e0d077f22.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/Part 1 - Data Cleaning.ipynb' "
    ],
    task_id="Part_1___Data_Cleaning",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "ust8898865!@",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Test_airflow-0305003702-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_a052ac6d_bddc_4a7d_9007_518e0d077f22 << op_1af79fd3_7724_4626_8c1e_625c7bda77f8


# Operator source: examples/pipelines/introduction-to-generic-pipelines/Part 2 - Data Analysis.ipynb
op_5fc8613c_e283_4484_92b1_ab53e2abb69b = KubernetesPodOperator(
    name="Part_2___Data_Analysis",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio_nginx_1:9000 --cos-bucket airflow --cos-directory 'Test_airflow-0305003702' --cos-dependencies-archive 'Part 2 - Data Analysis-5fc8613c-e283-4484-92b1-ab53e2abb69b.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/Part 2 - Data Analysis.ipynb' "
    ],
    task_id="Part_2___Data_Analysis",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "ust8898865!@",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Test_airflow-0305003702-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5fc8613c_e283_4484_92b1_ab53e2abb69b << op_a052ac6d_bddc_4a7d_9007_518e0d077f22


# Operator source: examples/pipelines/introduction-to-generic-pipelines/Part 3 - Time Series Forecasting.ipynb
op_e2828d4d_3b21_4683_8311_3a5bebf66738 = KubernetesPodOperator(
    name="Part_3___Time_Series_Forecasting",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.6.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio_nginx_1:9000 --cos-bucket airflow --cos-directory 'Test_airflow-0305003702' --cos-dependencies-archive 'Part 3 - Time Series Forecasting-e2828d4d-3b21-4683-8311-3a5bebf66738.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/Part 3 - Time Series Forecasting.ipynb' "
    ],
    task_id="Part_3___Time_Series_Forecasting",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "ust8898865!@",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "Test_airflow-0305003702-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e2828d4d_3b21_4683_8311_3a5bebf66738 << op_a052ac6d_bddc_4a7d_9007_518e0d077f22
