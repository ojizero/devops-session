import json
import boto3
import os

table_name = os.environ['DYNAMODB_TABLE']

def increment(event, context):
    client = boto3.client('dynamodb')

    response = client.get_item(
        TableName=table_name,
        Key={
            'id': {
                'S': 'hello',
            },
        },
    )

    count = int(response['Item']['count']['N']) + 1

    client.put_item(
        TableName=table_name,
        Item={
            'id': {
                'S': 'hello',
            },
            'count': {
                'N': str(count)
            }
        }
    )

    return {
        'statusCode': 404,
        'body': json.dumps({ 'new_count': count }),
    }

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
