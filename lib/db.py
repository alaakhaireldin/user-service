import os
import boto3

USERS_TABLE = os.environ['USERS_TABLE']

dynamodb_resource = boto3.resource('dynamodb', region_name="eu-north-1")

if os.environ.get('IS_OFFLINE'):
    dynamodb_resource = boto3.resource('dynamodb', region_name="localhost", endpoint_url='http://localhost:8000')

table = dynamodb_resource.Table(USERS_TABLE)
