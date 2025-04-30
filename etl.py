from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext

# Initialize Spark and Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Read from Glue Catalog
movies = glueContext.create_dynamic_frame.from_catalog(
    database="default",
    table_name="moviestmdb_5000_movies_csv"
)

# Convert to DataFrame for processing
df = movies.toDF()

# Data Cleaning
df = df.dropna()
df = df.withColumnRenamed("vote_average", "rating")
df = df.withColumn("profit", df["revenue"] - df["budget"])

# Convert back to DynamicFrame
output_dynamic_frame = DynamicFrame.fromDF(df, glueContext, "output_dynamic_frame")

# Write to S3 bucket with correct path
glueContext.write_dynamic_frame.from_options(
    frame=output_dynamic_frame,
    connection_type="s3",
    connection_options={"path": "s3://movies-transformed-data/"},
    format="parquet"
)

job.commit()
