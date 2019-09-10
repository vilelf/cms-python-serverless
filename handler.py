import json

def hello(event, context):
    return {
        'body': json.dumps({'message': 'Hello world, serverless!!'}),
        'statusCode': 200
    }
