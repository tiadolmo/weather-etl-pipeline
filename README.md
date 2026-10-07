# Weather Data ETL Pipeline

A Python ETL pipeline that extracts weather data from an API, transforms the data, and loads it into a database.

## Extraction Section
- **Fetches Data:** Pulls weather forecasts from the Tomorrow.io API for target locations.
- **Transforms JSON:** Flattens nested JSON payloads into a structured Pandas DataFrame.
- **Error Handling & Logging:** Safely catches API failures and logs execution events to both the console and a log file.

## Project Status
🚧 Currently under development.

# Project Structure
weather-etl/
│
├── dags/
│   └── weather_pipeline.py
│
├── src/
│   └── weather_etl/
│       ├── extract.py
│       ├── load.py
│       └── config.py
│
├── dbt/
│   └── weather_analytics/
│       ├── dbt_project.yml
│       │
│       ├── models/
│       │   ├── staging/
│       │   │   ├── schema.yml
│       │   │   └── stg_weather.sql
│       │   │
│       │   └── marts/
│       │       ├── schema.yml
│       │       └── weather_daily.sql
│       │
│       ├── seeds/
│       ├── snapshots/
│       ├── macros/
│       └── tests/
│
├── tests/
│   ├── test_extract.py
│   └── test_load.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── README.md
└── docker-compose.yml
