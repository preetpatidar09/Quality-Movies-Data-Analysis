# Quality-Movies-Data-Analysis
its an end to end data engineering project on aws


Techstack used - AWS - s3 for storage
AWS - Lambda for trigger
AWS - sns for notification
AWS - Glue crawler and catalogue for data columns information
AWS - Glue ETL JOB for transformation
AWS - Athena for Query and analyze


![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/OIP.jpg?raw=true)


1st step - I create a IAM role that have all policies to run this techstack

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/image.png?raw=true)
2nd step - store raw data file in s3 bucket in this path s3://movies-data-raw/tmdb_5000_movies.csv

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20083857.png?raw=true)
3rd step - create another bucket for store transformed data

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20083912.png?raw=true)
4th step - create crawler on s3 object and fetch meta data and store in default database

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20083951.png?raw=true)
![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20084025.png?raw=true)
5th step - create a etl pipeline for transformation as given in glue.py

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20084050.png?raw=true)
6th step - get data on bucket transformed data in path s3://movies-transformed-data/part-00000-b5fa39f7-1cb8-4281-923b-ea0afdbdfd21-c000.snappy.parquet
in parquet format

![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20083912.png?raw=true)

7th step - run athena queries on the transformed data for analysis
![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20084252.png?raw=true)

8th step - triger lambda lambda.py for getting transformed data
![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/Screenshot%202025-05-01%20084314.png?raw=true)

9th step - sns for notification published by lamba and seen in SMS 
![image_alt](https://github.com/preetpatidar09/Quality-Movies-Data-Analysis/blob/main/WhatsApp%20Image%202025-05-01%20at%2013.53.19_1c2b0e57.jpg?raw=true)
