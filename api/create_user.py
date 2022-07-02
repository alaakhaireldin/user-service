import json
import logging 
from lib import todo_service

def handler(event, context):
  body = json.loads(event['body'])

  if 'name' not in body:
    error_description = "Validation failed, the name is not in the request body"
    logging.error(error_description)
    raise Exception(error_description)

  if 'age' not in body:
    error_description = "Validation failed, the age is not in the request body"
    logging.error(error_description)
    raise Exception(error_description)
  
  todo_service.create_user_in_db(name, age)

  return { "statusCode": 200, "body": { "created": True } }

  
