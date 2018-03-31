import os
import json
import boto3

from random import randint

table_name = os.environ['DYNAMO_TABLE']

def increment (event, context):
    client = boto3.client('dynamodb')

    visitor_id = event.get('queryStringParameters', {}).get('visitor_id', None)

    if visitor_id is None:
        visitor_id = event['requestContext']['identity']['sourceIp']

    old_visits = 0
    try:
        response = client.get_item(
            TableName = table_name,
            Key = {
                'visitor_id': {
                    'S': visitor_id,
                },
            },
            AttributesToGet = [
                'visits'
            ],
        )

        old_visits = response['Item']['visits']['N']
    except:
        pass

    response = client.put_item(
        TableName = table_name,
        Item = {
            'visitor_id': {
                'S': 'some static id for now',
            },
            'visits': {
                'N': str(old_visits + 1),
            },
        },
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response),
    }
