import json
from utils.response import make_response

def hello(event, context):
    return make_response(
        body={'message': 'Hello world, serverless!!'},
        status_code=200
    )
