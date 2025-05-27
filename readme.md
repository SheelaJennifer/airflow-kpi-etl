#  OrderInfo KPI ETL Pipeline with Apache Airflow

This project is built to demonstrate real-world orchestration using **Apache Airflow 3.0**. 
It extracts KPIs from a PostgreSQL-based order data table using **Python, Pandas**, and stores outputs as CSV reports.

---

##  Key Features

- DAG orchestrated using **Airflow 3.0**
- KPI extraction via **PythonOperator**
- Queries PostgreSQL using `psycopg2`
- Output KPIs stored as CSVs in `/dags/kpi_output/`
- Structured logging and task retry enabled

---

##  Project Structure

```bash
airflow/
├── dags/
│   ├── orderinfo_etl_dag.py         # DAG definition
│   ├── scripts/
│   │   └── kpi_analysis.py          # Python script to compute KPIs
│   └── kpi_output/                  # CSV output reports
├── data/                            # Optional: raw sample data
├── logs/                            # Airflow logs
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview


## Setup Instructions
1. **Clone the repository**:
   ```bash

git clone https://github.com/your-username/orderinfo-airflow-kpi.git
cd orderinfo-airflow-kpi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. **Configure Airflow**:

export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create --username admin --firstname Sheela --lastname Jennifer --role Admin --email your@email.com
airflow webserver --port 8080

# In a new terminal
airflow scheduler

3. **Postgres Setup**:
Ensure you have a PostgreSQL instance running and create a database named `orderinfo_db`.

4. **Run the DAG**:
Access the Airflow UI at `http://localhost:8080` and trigger the `orderinfo_etl_dag`.





