import json
import boto3
import csv

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = 'Students'

def lambda_handler(event, context):

    # DEBUG: print event
    print("EVENT:", event)

    # check if triggered from S3
    if "Records" not in event:
        return {
            "statusCode": 200,
            "body": "Not an S3 event - test ignored"
        }

    table = dynamodb.Table(TABLE_NAME)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    lines = response['Body'].read().decode('utf-8').splitlines()

    csv_reader = csv.DictReader(lines)

    for row in csv_reader:
        table.put_item(Item={
            'studentId': row['studentId'],
            'name': row['name'],
            'department': row['department'],
            'marks': row['marks']
        })

    return {
        'statusCode': 200,
        'body': 'CSV processed successfully!'
    }