import json
import logging
from lib.todo_service import get_user_from_db


def handler(event, context):
  pathParameters = json.loads(event["pathParameters"])

  user_id = pathParameters["user_id"]

  user = get_user_from_db(user_id)

  return { "statusCode": 200, "body": { "user": user } }

# api.com/getUser/