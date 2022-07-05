import uuid
from lib.db import table

def generate_user_id():
  return str(uuid.uuid4())

def get_user_from_db(user_id):
  result = table.get_item(Key={ 'userId': user_id })
  item = result.get('Item')
  print(item)
  return item

def create_user_in_db(name, age):
  user_id = generate_user_id()
  # using table way, which is table = db.table. The table way helps to infer, figure out, the types of the keys. where table = boto3.resource('dynamodb', region_name="eu-norht-1").Table(USERS_TABLE)
  item = { 'userId': user_id, 'name': name, 'age': int(age) }
  table.put_item(Item=item)
  return user_id
