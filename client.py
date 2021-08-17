import boto3
from time import time
import scraper.getRecords as gr

def main():
    return gr.getData()

if __name__ == "__main__":
    data = main()
    print(data)
