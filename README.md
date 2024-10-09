# Sales Data ETL Pipeline

## Project Overview
The Sales Data ETL Pipeline is designed to extract, transform, and load sales data from multiple sources into a PostgreSQL data warehouse for analysis. The pipeline ensures high-quality data processing and provides valuable insights through monthly sales aggregation.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)

## Technologies Used
- **Python**: Core programming language for the ETL process.
- **Pandas**: Data manipulation and analysis library.
- **SQL**: Query language for interacting with the PostgreSQL database.
- **Apache Airflow**: Workflow orchestration tool for scheduling and managing ETL tasks.
- **PostgreSQL**: Data warehouse for storing the cleaned and aggregated data.

## Features
- **Data Extraction**: Pulls data from CSV files and other sources.
- **Data Transformation**: Cleans and processes the data to ensure quality.
- **Monthly Aggregation**: Summarizes sales data on a monthly basis.
- **Automated Workflow**: Uses Apache Airflow for efficient task scheduling.

## Installation
To run the Sales Data ETL Pipeline locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/christymugs/datapipeline.git
   cd datapipeline
2. **Set up a virtual Environment**
      ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
     ```bash
   pip install pandas apache-airflow psycopg2-binary


## Usage
To run the ETL pipeline, execute the following scripts in order:

1. **Extract Data**:
   ```bash
   python extract_from_csv.py
   
2. **Transform Data**
      ```bash
   python transform_data.py

3. **Load Data: Make sure the transformation script handles loading into PostgreSQL**

## Data Source
The sales data is sourced from sales_data.csv on Kaggle. Ensure this file is placed in the project directory for successful extraction.
   https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

<img width="505" alt="Screenshot 2024-10-09 at 2 31 07 AM" src="https://github.com/user-attachments/assets/ecb154a6-c663-4dbb-b239-fff45c995c88">

