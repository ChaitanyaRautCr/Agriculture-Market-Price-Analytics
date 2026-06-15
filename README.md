# Agriculture Market Price Analytics

## Project Overview

Agriculture Market Price Analytics is an end-to-end Data Engineering and Analytics project that processes agricultural crop price data using Python, PostgreSQL, SQL, and Power BI.

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Power BI
* Git & GitHub

## Features

* ETL Pipeline (Extract, Transform, Load)
* Data Cleaning and Transformation
* PostgreSQL Database Integration
* SQL Analysis Queries
* Interactive Power BI Dashboards
* Crop and Market Price Analytics

## Architecture

Raw CSV Data
→ Extract (Python)
→ Transform (Pandas)
→ Load (PostgreSQL)
→ SQL Analysis
→ Power BI Dashboard

## Dashboard Pages

### Executive Overview

![Executive Overview](executive_overview.png.png)

### Crop Insights

![Crop Insights](crop_insights.png.png)

## Setup

### Configure PostgreSQL Password

Windows PowerShell:

```powershell
$env:DB_PASSWORD="your_password"
python etl/load.py
```

### Run ETL

```bash
python etl/extract.py
python etl/transform.py
python etl/load.py
```
