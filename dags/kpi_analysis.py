import psycopg2
import pandas as pd

def run_kpi_analysis():

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="webtrace",
        user="postgres",
        password="sheela"
    )

    queries = {
        "total_orders": "SELECT COUNT(*) AS total_orders FROM orderinfo_bq;",
        "total_items": "SELECT SUM(num_of_item) AS total_items FROM orderinfo_bq WHERE is_cancelled = false;",
        "daily_order_volume": """
            SELECT DATE(created_at) AS order_date, COUNT(*) AS daily_orders
            FROM orderinfo_bq
            GROUP BY order_date
            ORDER BY order_date;
        """,
        "avg_items_per_order": "SELECT AVG(num_of_item) AS avg_items FROM orderinfo_bq WHERE is_cancelled = false;",
        
        "returned_orders": "SELECT COUNT(*) AS returned_orders FROM orderinfo_bq WHERE returned_at IS NOT NULL;",
        "avg_delivery_days": "SELECT ROUND(AVG(delivery_duration_days)::numeric, 2) AS avg_days FROM orderinfo_bq WHERE delivery_duration_days IS NOT NULL;",

  #      "avg_delivery_days": "SELECT ROUND(AVG(delivery_duration_days), 2) AS avg_days FROM orderinfo_bq WHERE delivery_duration_days IS NOT NULL;",
        "hourly_orders": """
            SELECT EXTRACT(HOUR FROM created_at) AS hour, COUNT(*) AS orders
            FROM orderinfo_bq
            GROUP BY hour ORDER BY orders DESC;
        """,
        "orders_by_gender": "SELECT gender, COUNT(*) AS total_orders FROM orderinfo_bq GROUP BY gender;",
        "ship_vs_delivered": "SELECT COUNT(shipped_at) AS shipped_orders, COUNT(delivered_at) AS delivered_orders FROM orderinfo_bq;"
    }

    for kpi_name, query in queries.items():
        df = pd.read_sql_query(query, conn)
        df.to_csv(f"/home/sheela/airflow/dags/kpi_output/{kpi_name}.csv", index=False)

    conn.close()
