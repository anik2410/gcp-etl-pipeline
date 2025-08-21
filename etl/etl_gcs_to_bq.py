import os
import io
import pandas as pd
from google.cloud import storage, bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/anik/projects/gcp-etl-pipeline/etl/keys/etl-service-key.json"


BUCKET_NAME = "anik-gcs-bucket-1"
SOURCE_FILE = "customers-100.csv"
BQ_DATASET = "etl_demo_dataset"
BQ_TABLE = "processed_data"


storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)
blob = bucket.blob(SOURCE_FILE)

print("Downloading file from GCS...")
data_bytes = blob.download_as_bytes()

df = pd.read_csv(io.BytesIO(data_bytes))
print("Data loaded into data frame...")
print(df.head())

df["processed_column"] = df[df.columns[0]].apply(lambda x:str(x).upper())

bq_client = bigquery.Client()

table_ref = f"{bq_client.project}.{BQ_DATASET}.{BQ_TABLE}"

print(f"Uploading to BigQuery table: {table_ref} ...")
job = bq_client.load_table_from_dataframe(df, table_ref)

job.result()

print("ETL process completed.")