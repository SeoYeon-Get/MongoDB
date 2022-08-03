# 'author': 'Lee', 'text' : 'Who are you?'인 데이터를 찾아서
# 'author': 'Park', 'address' : 'Busan' 로 변경
# 만약 address 칼럼이 없다면 만들어서 넣어준다.
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['test-db']

# data = {
#      'author' : 'lee',
#      'text' : 'Who are you?',
#  }
# dpInsert = db.posts.insert_one(data)

db['posts'].update(
     { 'author': 'lee', 'text' : 'Who are you?' },
     { "$set":{'author': 'Lee', 'address' : 'Busan' }} )


