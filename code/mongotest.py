import pymongo
client = pymongo.MongoClient("localhost",27017)
mongo_python = client.python
mongo_stu = mongo_python.stu
mongo_stu.insert_one({"name":'郭靖',"age":18})
mongo_stu.update({"name":'郭靖'},{"$set":{"name":"杨康"}})
cur=mongo_stu.find_one()
print(cur)
