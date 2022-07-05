import logging
import json

def get_http_error(status_code, message):
    logging.error(message)
    return { "statusCode": status_code, "body": json.dumps({ "error": message }) }