import pymango

connection_url=pymongo.MongoClient("mongodb://localhost:27017/")
db_name=connection_url["automation_config"]
print(db_name)
collection_name=db_name["config"]
print(collection_name)
collection_data=collection_name.insert_one({"username":"rafik.boudalia@yassir.com","password":"SparkyDz@1234"})

print(collection_data)