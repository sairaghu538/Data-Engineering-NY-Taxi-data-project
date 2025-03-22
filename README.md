# Data-Engineering-NY-Taxi-data-project

Module 1: Infrastructure & Database Setup in GCP
✅ Introduction to GCP
Set up a free-tier GCP account.
Enable required services: Cloud Storage, BigQuery, Pub/Sub, Cloud Composer, and Dataflow.
✅ Database Setup (PostgreSQL on GCP Cloud SQL instead of Docker)
Create a Cloud SQL (PostgreSQL) instance.
Connect to Cloud SQL using pgAdmin or the Cloud Shell.
Load sample data (NY Taxi dataset or any structured dataset).
✅ Infrastructure as Code (Terraform in GCP)
Write Terraform scripts to automate infrastructure setup.
Deploy Cloud SQL, BigQuery, and Pub/Sub using Terraform.
Store Terraform state in Google Cloud Storage.
📌 Homework
Deploy PostgreSQL instance using Terraform.
Connect to the database and execute basic SQL queries.

![1](https://github.com/user-attachments/assets/5f0ce45f-1e37-4870-bd8e-e5b0494a3a35)




Module 2: Workflow Orchestration with GCP Cloud Composer
✅ Introduction to Data Lakes & Workflow Orchestration
Use Cloud Storage as a Data Lake.
Automate workflows with Cloud Composer (Apache Airflow in GCP).
✅ Workflow Orchestration using Cloud Composer (instead of Kestra)
Create a DAG in Cloud Composer to automate data ingestion.
Schedule jobs to move data from Cloud Storage to BigQuery.
📌 Homework
Create an Airflow DAG to move raw data from Cloud Storage to BigQuery.
Workshop 1: Data Ingestion (Replacing Local API Calls with GCP Services)
✅ API Data Extraction using Cloud Functions
Fetch external API data using Cloud Functions instead of running scripts locally.
Store raw data in Cloud Storage.
✅ Data Normalization & Incremental Loading in BigQuery
Use Dataflow (Apache Beam on GCP) to clean and transform data.
Store transformed data in BigQuery tables for analysis.
📌 Homework
Write a Cloud Function to pull data from an API and store it in Cloud Storage.
Use Dataflow to process and move data into BigQuery.

Module 3: Data Warehousing with BigQuery
✅ Introduction to BigQuery & Best Practices
Learn BigQuery SQL syntax.
Partitioning & Clustering for optimized query performance.
✅ Machine Learning in BigQuery (Optional)
Use BigQuery ML for simple predictive models.
📌 Homework
Optimize a BigQuery table with partitioning & clustering.

Module 4: Analytics Engineering with dbt & Metabase
✅ Using dbt in GCP (instead of running dbt locally)
Deploy dbt Cloud (free-tier) instead of local installation.
Transform data in BigQuery using dbt models.
✅ Data Visualization with Metabase
Connect Metabase to BigQuery for interactive dashboards.
📌 Homework
Create dbt models for transforming raw data.
Build a dashboard in Metabase.

Module 5: Batch Processing with Apache Spark on GCP
✅ Running Apache Spark in GCP Dataproc
Deploy a free-tier Dataproc cluster for Spark processing.
Process large datasets using PySpark or Spark SQL.
📌 Homework
Run a batch transformation job using PySpark on Dataproc.

Module 6: Streaming Data Processing with Kafka on GCP
✅ Streaming with Pub/Sub & Dataflow (Replacing Kafka)
Use Google Pub/Sub as a messaging system.
Process streaming data using Cloud Dataflow (Apache Beam).
📌 Homework
Publish & consume messages using Pub/Sub.
Process real-time data streams with Cloud Dataflow.



