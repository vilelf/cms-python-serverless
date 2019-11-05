import json
from utils.response import make_response

def hello(event, context):
    return make_response(
        {'message': 'Hello world, serverless!!'},
        200
    )
