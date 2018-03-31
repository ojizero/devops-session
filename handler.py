import os
import json
import boto3

from random import randint

def insert_to_dynamo(event, context):
    client = boto3.client('dynamodb')

    response = client.put_item(
        TableName = os.environ['DYNAMO_TABLE'],
        Item = {
            'visitor_id': {
                'S': 'some static id for now',
            },
            'visits': {
                'N': randint(10, 1000),
            },
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response),
    }
