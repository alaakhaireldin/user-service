import json
import logging
from lib.todo_service import get_user_from_db


def handler(event, context):
  body = json.loads(event['body'])

  if 'user_id' not in body:
    error_description = "Validation failed, the user id is not in the request body"
    logging.error(error_description)
    raise Exception(error_description)

  get_user_from_db(user_id)

  return { "statusCode": 200, "body": { "created": True } }
