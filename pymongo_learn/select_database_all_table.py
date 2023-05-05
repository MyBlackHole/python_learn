from pymongo import MongoClient

# 服务链接
mongodb_link = MongoClient(
    host="127.0.0.1",
    port=27017,
    username="root",
    password="3edc#EDC",
)


udal = mongodb_link["udal"]
collections = udal.list_collection_names()
print(collections)
for collection in collections:
    print(collection)
    data = udal[collection].find()
    print(list(data))
    print("*" * 300)
