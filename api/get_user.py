import simplejson
import logging
from lib.todo_service import get_user_from_db


def handler(event, context):
  user_id = event['pathParameters']['user_id']
  user = get_user_from_db(user_id)

  if not user:
    return { "statusCode": 404, "body": simplejson.dumps({ "message": f"{user_id} does not exist." }) }

  return { "statusCode": 200, "body": simplejson.dumps({ "user": user }) }

# api.com/getUser/