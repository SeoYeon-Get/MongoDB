from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['test-db']
#print(client.list_database_names())

# data = {
#     'author' : 'moon',
#     'text' : 'mongoDB is first',
#     'tags' : ['kwangwoon', 'python', 'pymongo']
# }

# dpInsert = db.posts.insert_one(data)

for d in db['posts'].find():
    print(d['author'], d['text'], d['tags'])
    
print(db.posts.find_one({'author':'hun'})['text'])
