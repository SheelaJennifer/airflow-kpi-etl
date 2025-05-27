import pandas as pd

def clean_and_merge():
    cancelled_df = pd.read_csv(
        "/home/sheela/airflow/data/orders_cancld.csv",
        parse_dates=['created_at', 'returned_at', 'shipped_at', 'delivered_at']
    )

    complete_df = pd.read_csv(
        "/home/sheela/airflow/data/orders_succ.csv",
        parse_dates=['created_at', 'returned_at', 'shipped_at', 'delivered_at']
    )

    cancelled_df['is_cancelled'] = True
    complete_df['is_cancelled'] = False

    combined_df = pd.concat([cancelled_df, complete_df], ignore_index=True)

    datetime_cols = ['created_at', 'returned_at', 'shipped_at', 'delivered_at']
    for col in datetime_cols:
        combined_df[col] = pd.to_datetime(combined_df[col], errors='coerce')
        combined_df[col] = combined_df[col].dt.tz_localize(None)

    combined_df['delivery_duration_days'] = (
        combined_df['delivered_at'] - combined_df['shipped_at']
    ).dt.days

    combined_df.to_csv("/home/sheela/airflow/data/cleaned_orders.csv", index=False)
    print("Data cleaned and saved as 'cleaned_orders.csv'")
