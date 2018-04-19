import json
import boto3

def increment(event, context):
    client = boto3.client('dynamodb')

    client.put_item(
        TableName='users_table',
        Item={
            'id': {
                'S': 'hello',
            },
            'count': {
                'N': '0',
            },
        },
    )

    return {
        'statusCode': 200,
        'body': json.dumps({ 'hello': 'annajah' }),
    }

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
