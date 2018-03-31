import os
import json
import boto3

from random import randint

table_name = os.environ['DYNAMO_TABLE']

def increment (event, context):
    client = boto3.client('dynamodb')

    visitor_id = event['requestContext']['identity']['sourceIp']

    query_string = event.get('queryStringParameters')

    if query_string is not None and 'visitor_id' in query_string:
        visitor_id = query_string.get('visitor_id')

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

        old_visits = int(response['Item']['visits']['N'])
    except:
        pass

    response = client.put_item(
        TableName = table_name,
        Item = {
            'visitor_id': {
                'S': str(visitor_id),
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

def get_counts (event, context):
    client = boto3.client('dynamodb')

    visitor_id = event['requestContext']['identity']['sourceIp']

    query_string = event.get('queryStringParameters')

    if query_string is not None and 'visitor_id' in query_string:
        visitor_id = query_string.get('visitor_id')

        response = client.get_item(
            TableName = table_name,
            Key = {
                'visitor_id': {
                    'S': visitor_id,
                },
            },
        )

        response = {
            'items': [response['Item']],
        }
    else:
        response = {
            'items': client.scan(TableName = table_name)['Items'],
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response),
    }
