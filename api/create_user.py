import json
import logging 
from lib import todo_service
from lib.error import get_http_error

def handler(event, context):
  body = event['body']

  if body is None:
    return get_http_error(400, "Must include a body with the request")

  parsedBody = json.loads(body)

  if 'name' not in parsedBody:
    return get_http_error(400, "Validation failed, the name is not in the request body")

  if 'age' not in parsedBody:
    return get_http_error(400, "Validation failed, the age is not in the request body")
  
  name = parsedBody["name"]
  age = parsedBody["age"]
  user_id = todo_service.create_user_in_db(name, age)
  return { "statusCode": 200, "body": json.dumps({ "userId": user_id }) }

  
