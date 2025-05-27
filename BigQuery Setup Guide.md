# 📁 BigQuery Setup Guide

This guide explains how to configure your local environment to pull real-time, large-scale data from **Google BigQuery**, which can be used as input for your Airflow ETL pipeline.

---

## 📌 Why Use BigQuery?

- Access to **extensive public datasets**
- **Scalable and serverless** architecture
- Ideal for **real-time production-grade testing**
- Seamless **Python SDK integration**

---

## 📦 Prerequisites

### 🔐 1. Google Cloud Platform (GCP) Setup

1. Go to [https://console.cloud.google.com](https://console.cloud.google.com)
2. Sign in with your Google account.
3. Click on the top project dropdown → **"New Project"**
   - Name it something like `airflow-revenue-report`
4. After creation, ensure it's selected as the current project.
5. Navigate to **APIs & Services → Library**
   - Search for **BigQuery API**
   - Click **Enable**

---

### 🧾 2. Authenticate Using Google Cloud CLI (Recommended)

> ✅ No service account or JSON key required for this flow.

#### a. Install the Google Cloud CLI:

Follow the official instructions:  
👉 [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)

#### b. Authenticate via browser:
```bash
gcloud auth login
```

#### c. Set your active project:
```bash
gcloud config set project airflow-revenue-report
```

#### d. Enable BigQuery API (if not already):
```bash
gcloud services enable bigquery.googleapis.com
```

3. 🐍 Python Requirements

Install the BigQuery Python client:
```bash
pip install google-cloud-bigquery
```