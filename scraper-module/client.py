import boto3
import getRecords as gr

def handler():
    DB_NAME = "polyscrubsdb"
    TBL_NAME = "machinedata"

    #Choses default aws cli profile, change profile_name to use a different profile
    client = boto3.Session(profile_name="default").client('timestream-write')

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

