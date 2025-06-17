'''
=================================================
Milestone 3

Nama  : Nur M Assudais Alkharomain
Batch : RMT-041

This program is designed to automate the process of loading data from PostgreSQL, performing data cleaning, and posting the data to Elasticsearch for data visualization.
The data used in this program is about the behaviour, preferences, and churn patterns of MTN Nigeria customers in Q1 2025.

=================================================
'''

#Library needed for this program
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2
from elasticsearch import Elasticsearch

def fetchData():

    '''
    This function is intended to retrieve data from PostgreSQL and convert the data.
    It will generate a CSV file that will be used for data cleaning.
    '''


    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )
    sql = 'SELECT * FROM table_m3;'
    df = pd.read_sql(sql, conn)
    df.to_csv('/opt/airflow/dags/P2M3_Dais_data_raw.csv', sep=',', index=False)
    conn.close()

def data_cleaning():
    ''' 
    This function is used to clean a dataframe by removing duplicates,
    converting column titles to lowercase, replacing spaces with underscores,
    removing symbols, and handling missing values.
    '''
    df=pd.read_csv('/opt/airflow/dags/P2M3_Dais_data_raw.csv')
    df.drop_duplicates(inplace=True) # Duplicate Handling
    df.columns = df.columns.str.lower()  # Transform all letters become lowercase
    df.columns = df.columns.str.replace(' ', '_')  # Transform space with underscore
    df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_]', '')  # Remove unnecessary symbol (if any)
    df['date_of_purchase'] = pd.to_datetime(df['date_of_purchase'], format="%b-%y").dt.strftime("%B") # Change to datetime format
    df['reasons_for_churn'] = df['reasons_for_churn'].fillna('None') # Fill missing values on column 'Reasons for Churn' with 'None'
    df.to_csv('/opt/airflow/dags/P2M3_Dais_data_clean.csv', index = False)

def insertElasticsearch():
    ''' 
    This function is used to load cleaned data into Elasticsearch for data visualization using Kibana.
    '''
    es = Elasticsearch("http://elasticsearch:9200", timeout=60)  # Add timeout up to 60 sec
    df=pd.read_csv('/opt/airflow/dags/P2M3_Dais_data_clean.csv')
    for i,r in df.iterrows():
        doc=r.to_dict()
        res=es.index(index="for_visualization_kibana", body=doc)
        print(res)
	

default_args= {
    'owner': 'Dais',
    'start_date': dt.datetime(2024, 11, 2, 9, 10, 0) - timedelta(hours=7),
    'retries': 1,  # Added retry mechanism
    'retry_delay': timedelta(minutes=5),    
}

with DAG(
    "P2M3_Dais_DAG",
    description='Fetching Data, Cleaning Data, and Post to Elasticsearch',
    default_args=default_args,
    schedule_interval='10-30/10 9 * * 6',
    ) as dag:

    fetch_data = PythonOperator(
        task_id='fetch_data',
        python_callable=fetchData,
    )

    clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=data_cleaning,
    )
    
    post_data = PythonOperator(
        task_id='post_to_Elasticsearch',
        python_callable=insertElasticsearch
    )


    fetch_data >> clean_data >> post_data