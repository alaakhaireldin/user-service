import json
import logging 
from lib import todo_service

def handler(event, context):
  print(event)

  body = event['body']

  if body is None:
    error_description = "Must include a body with the request"
    logging.error(error_description)
    return { "statusCode": 400, "body": json.dumps({ "error": error_description }) }

  parsedBody = json.loads(body)

  if 'name' not in parsedBody:
    error_description = "Validation failed, the name is not in the request body"
    logging.error(error_description)
    return { "statusCode": 400, "body": json.dumps({ "error": error_description }) }

  if 'age' not in parsedBody:
    error_description = "Validation failed, the age is not in the request body"
    logging.error(error_description)
    return { "statusCode": 400, "body": json.dumps({ "error": error_description }) }
  
  name = parsedBody["name"]
  age = parsedBody["age"]

  user_id = todo_service.create_user_in_db(name, age)

  return { "statusCode": 200, "body": json.dumps({ "userId": user_id }) }

  
