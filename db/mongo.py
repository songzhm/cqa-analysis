from pymongo import MongoClient
from pprint import pprint


# Collections:
# 1. questionByTag
# 2. answerByQuestion
# 3. votterByAnswer

client = MongoClient()
db = client.test

db.questionByTag.delete_many({})
db.answerByQuestion.delete_many({})

print db.questionByTag.count()
print db.answerByQuestion.count()


# query data
cursor = db.questionByTag.find()

question_threshold = 1
count = 0
for document in cursor:
    pprint(document)
    count+=1
    if count>=question_threshold:
        break

cursor = db.answerByQuestion.find()

answer_threshold = 1
count = 0
for document in cursor:
    pprint(document)
    count+=1
    if count>=answer_threshold:
        break