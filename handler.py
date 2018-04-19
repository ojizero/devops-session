import json
import boto3

def increment(event, context):
    client = boto3.client('dynamodb')

    response = client.get_item(
        TableName='users_table',
        Key={
            'id': {
                'S': 'hello',
            },
        },
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response),
    }

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
