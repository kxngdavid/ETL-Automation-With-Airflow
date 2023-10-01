# importing relevant libraries for this project
import json
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import datetime, timedelta
import configparser
from pandas.io.json import json_normalize
from sqlalchemy import create_engine
import os

# function to fetch and transform data from the api
def get_jokes():
    url = r"https://official-joke-api.appspot.com/random_ten"
    response = requests.get(url)
    data = json.loads(response.text)

    # this normalizes the semi-structured data and turns it into a dataframe
    dataframe = json_normalize(data=data)
    return dataframe

# function to insert the data into the database
def insert_data():

    #getting absolute path of current directory
    current_dir = os.path.dirname(__file__)

    #building the absolute file path for the config file
    config_file_path = os.path.join(current_dir, 'db_config_airflow.txt')

    # creating a Configparser object
    config = configparser.ConfigParser()

    # reading the configuration file
    config.read(config_file_path)

    # reading credentials from file
    username = config.get(
        'Credentials', 
        'username')

    host = config.get(
        'Credentials', 
        'host')

    password = config.get(
        'Credentials',
        'password')

    port = config.get(
        'Credentials', 
        'port')

    db_name = config.get(
        'Credentials',
        'db_name')

    engine = create_engine(
        'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            username,
            password,
            host,
            port,
            db_name
        ))

    # creating a raw connection to the database
    connection = engine.raw_connection()
    cursor = connection.cursor()

    #saving the data from the get_jokes function into a variable
    dataframe = get_jokes()

    # pushing the data into the database
    try:
        for _, row in dataframe.iterrows():
            cursor.execute(
                "INSERT INTO jokes_data (id, type, setup, punchline) VALUES (%s, %s, %s, %s)",
                (
                row[
                    "id"],
                row[
                    "type"],
                row[
                    "setup"],
                row[
                    "punchline"]),
            )
    except Exception as error:
        print(error)

    connection.commit()
    cursor.close()
    connection.close()

# defining default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 10, 1),
    "retries": 3,
}

# defining the DAG
dag = DAG(
    "get_jokes_and_insert_into_postgres",
    default_args=default_args,
    description="Get jokes from the Random Jokes Ten API and insert into PostgreSQL",
    schedule_interval=timedelta(minutes=2),
)

# defining our tasks 
t1 = PythonOperator(task_id="get_jokes", python_callable=get_jokes, dag=dag)

t2 = PythonOperator(task_id="insert_data", python_callable=insert_data, dag=dag)

# defining the dependencies of our tasks
t1 >> t2
