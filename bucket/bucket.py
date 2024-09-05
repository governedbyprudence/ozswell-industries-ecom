import os
import boto3
# Bucket Details from .env file
BUCKET_NAME = os.environ.get("BUCKET_NAME")
BUCKET_ACCESS_KEY = os.environ.get("BUCKET_ACCESS_KEY")
BUCKET_SECRET_KEY = os.environ.get("BUCKET_SECRET_KEY")
BUCKET_REGION = os.environ.get("BUCKET_REGION")
BUCKET_ENDPOINT = os.environ.get("BUCKET_ENDPOINT")

# get Bucket Client singleton

def get_bucket_client():
    s3 = boto3.client(
        service_name="s3",
        aws_access_key_id=BUCKET_ACCESS_KEY,
        aws_secret_access_key=BUCKET_SECRET_KEY,
        region_name=BUCKET_REGION,
        endpoint_url=BUCKET_ENDPOINT
    )
    
    return s3   

bucket_client = get_bucket_client()