from lib.error import get_http_error
import json


def test_error_function():
    message = "things didn't work"
    expected_results = { "statusCode": 400, "body": json.dumps({ "error": message }) }
    assert get_http_error(400, message) == expected_results