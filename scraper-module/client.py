import boto3
import getRecords as gr

def handler(event=None, context=None):
    DB_NAME = "polyscrubsdb"
    TBL_NAME = "machinedata"

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
    handler()

