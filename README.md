# aviation-telemetry-pipeline

Aviation Telemetry & Maintenance Data Pipeline

Overview

This is my portfolio project aimed at landing my first role as a Junior Data Engineer.  
The main goal of this project is to build an automated data pipeline that fetches real-time flight telemetry from the public OpenSky Network API, cleans and processes the data, and prepares it for analytical reporting.  
The business focus is to help detect flight anomalies (such as sudden altitude drops) and assist in monitoring overall aircraft fleet health.  

Data Architecture (Medallion Pattern)

The pipeline processes data through three main layers (Bronze, Silver, Gold):  

1. Ingestion / Bronze (Raw Data): A Python script fetches raw telemetry data from the OpenSky API and saves raw JSON files into AWS S3, partitioned by date.  
2. Silver (Cleaned Data): PySpark reads the JSON files, enforces schemas, cleans out invalid GPS/null values, and saves the data as optimized Parquet files.  
3. Gold (Analytics Ready): dbt (SQL) builds analytical dimensions and fact tables, calculating safety risk flags and fleet metrics.  
4. Visualization: Power BI connects to the Gold layer to display fleet status and risk insights.
```
[ OpenSky API ] 
       │
       ▼ (Python Script)
[ AWS S3 - Bronze (JSON) ] 
       │
       ▼ (PySpark)
[ AWS S3 - Silver (Parquet) ] 
       │
       ▼ (dbt / SQL)
[ Postgres / Warehouse - Gold ] 
       │
       ▼
[ Power BI Dashboard ]
```
Tech Stack

 Languages: Python, SQL  
 Data Processing: PySpark, dbt  
 Storage & Warehousing: AWS S3, PostgreSQL  
 Orchestration & Containerization: Apache     Airflow, Docker  
 Business Intelligence: Power BI  

Quick Start Guide

Prerequisites
 Docker and Docker Compose installed.
 AWS Account (or local S3 emulator like MinIO).


