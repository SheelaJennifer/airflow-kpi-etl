from google.cloud import bigquery
import pandas as pd

def pull_orders_sample():
    client = bigquery.Client(project="airflow-revenue-report")
    query = "SELECT * FROM `bigquery-public-data.thelook_ecommerce.orders` LIMIT 1000"
    df = client.query(query).to_dataframe()
    df.to_csv("/home/sheela/airflow/data/orders_cancld.csv", index=False)
    print("Data pulled and saved as orders_sample.csv")
