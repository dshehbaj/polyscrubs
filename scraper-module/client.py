import boto3
from time import time
import getRecords as gr
import os

def main():
    DB_NAME = os.environ['DB_NAME']
    TBL_NAME = os.environ['TBL_NAME']
    client = boto3.client('timestream-write')
    data = gr.getData()
    for records in data.values():
        client.write_records(
            DatabaseName=DB_NAME,
            TableName=TBL_NAME,
            Records=records
        )

