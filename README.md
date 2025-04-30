# Quality-Movies-Data-Analysis
its an end to end data engineering project on aws


Techstack used - AWS - s3 for storage
AWS - Lambda for trigger
AWS - sns for notification
AWS - Glue crawler and catalogue for data columns information
AWS - Glue ETL JOB for transformation
AWS - Athena for Query and analyze

1st step - I create a IAM role that have all policies to run this techstack
2nd step - store raw data file in s3 bucket in this path s3://movies-data-raw/tmdb_5000_movies.csv
3rd step - create another bucket for store transformed data
4th step - create crawler on s3 object and fetch meta data and store in default database
5th step - create a etl pipeline for transformation as given in glue.py
6th step - get data on bucket transformed data in path s3://movies-transformed-data/part-00000-b5fa39f7-1cb8-4281-923b-ea0afdbdfd21-c000.snappy.parquet
in parquet format
7th step - run athena queries on the transformed data for analysis
8th step - triger lambda lambda.py for getting transformed data
9th step - sns for notification published by lamba and seen in SMS 

