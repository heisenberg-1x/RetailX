# RetailX 🛒

An end-to-end data engineering project simulating a real-world retail analytics pipeline. This project extracts messy, nested data from a REST API, stores it on Amazon S3, transforms it using AWS Glue (PySpark), loads it into Amazon Redshift, and orchestrates it with Apache Airflow.

## 🔧 Tech Stack
- Python (API extraction)
- Amazon S3 (raw data storage)
- AWS Glue (PySpark ETL)
- Amazon Redshift (data warehousing)
- Apache Airflow (orchestration)
- SQL (analytics)
- Tableau / QuickSight (optional visualization)

## 📁 Folder Structure

RetailX/
├── README.md
├── requirements.txt
├── /src/               # Python scripts (API extraction, transformation, loading)
├── /glue_jobs/         # AWS Glue PySpark scripts
├── /airflow_dags/      # Airflow DAGs
├── /redshift_sql/      # Table creation, copy commands, analytics queries
├── /notebooks/         # Jupyter notebooks (EDA, transformations, SQL testing)
├── /docs/              # Diagrams, schema images, project planning
└── /data_samples/      # Sample raw and cleaned data files (non-sensitive)
