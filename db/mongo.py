from pymongo import MongoClient


client = MongoClient()
db = client.test
db.questionByTag.delete_many({})
print db.questionByTag.count()

