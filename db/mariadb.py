import mysql.connector as mariadb
import json

with open('question.json','rb') as data_file:
    data = json.load(data_file)


mariadb_connection = mariadb.connect(user='ming', password = '', database='cqavoting')

cursor = mariadb_connection.cursor()

# f = open('IST343.sql','r')
# query = "".join(f.readlines())
# cursor.execute(query,multi = True)
# res = cursor.execute('show databases;')
# print(res)
# f.close()
cursor.execute("select * from QUESTION;")
results = cursor.fetchall()
print(results)


mariadb_connection.close()


def insertQuestion(cursor,data):
    