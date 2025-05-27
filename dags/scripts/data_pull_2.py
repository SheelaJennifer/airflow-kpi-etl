from google.cloud import bigquery
import pandas as pd

def pull_orders_complete():
    client = bigquery.Client(project="airflow-revenue-report")
    query = """
        SELECT order_id, user_id, status, gender, created_at, returned_at,
               shipped_at, delivered_at, num_of_item
        FROM `bigquery-public-data.thelook_ecommerce.orders`
        WHERE status = 'Complete'
        LIMIT 1000
    """
    df = client.query(query).to_dataframe()
    df.to_csv("/home/sheela/airflow/data/orders_succ.csv", index=False)
    print("Completed orders pulled and saved as orders_succ.csv")
