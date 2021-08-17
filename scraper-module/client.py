import boto3
from time import time
import getRecords as gr
import os
import secrets

def handler(event, context):
    if (event and context):
        DB_NAME = os.environ['DB_NAME']
        TBL_NAME = os.environ['TBL_NAME']
    else:
        DB_NAME = secrets.DB_NAME
        TBL_NAME = secrets.TBL_NAME
    client = boto3.client('timestream-write')
    data = gr.getData()
    for records in data.values():
        client.write_records(
            DatabaseName=DB_NAME,
            TableName=TBL_NAME,
            Records=records
        )
    return data

if __name__ == "__main__":
    handler(None, None)

