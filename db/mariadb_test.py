
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import mysql.connector as mariadb
import json






# def insertQuestion(cursor,data):
#     cursor.execute(u"INSERT INTO QUESTION (QUESTION_ID, \
# USER_ID, QUESTION, SUMMARY, ANSWER_COUNT, FOLLOWER_COUNT, \
# ARCHIVE_COUNT, DATA_CREATED, DATA_LAST_ANSWERED, QUESTION_URL, TAG\
# REPLY_COUNT, RECOMMEND_COUNT) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{}) \
# ".format(data['id'],data['author'],data['question'],data['summary'],data['answers_count'],data['followers_count'],data['archives_count'],data['date_created'],data['date_last_answered'],data['url'],data['tags'],data['replies_count'],data['recommends_count'])
# )

def insertQuestion(cursor,data):
    cursor.execute("SELECT QUESTION_ID FROM QUESTION WHERE QUESTION_ID = %s " % (data['id']))
    results = cursor.fetchall()

    if len(results)==0:
      cursor.execute("INSERT INTO QUESTION (QUESTION_ID,USER_ID, QUSETION, SUMMARY, ANSWER_COUNT,\
      FOLLOWER_COUNT,ARCHIVE_COUNT, DATA_CREATED, DATA_LAST_ANSWERED, QUESTION_URL,REPLY_COUNT,\
      RECOMMEND_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],data['author'],\
      data['question'],data['summary'],data['answers_count'],data['followers_count'],\
      data['archives_count'],data['date_created'],data['date_last_answered'],data['url'],\
      data['replies_count'],data['recommends_count']))

def insertAnswer(cursor,data):
    cursor.execute("SELECT ANSWER_ID FROM ANSWER WHERE ANSWER_ID = %s " % (data['id']))
    results = cursor.fetchall()
    
    if len(results)==0:
        cursor.execute("INSERT INTO ANSWER (ANSWER_ID, QUESTION_ID, USER_ID, CONTENT, ANSWER_HTML,\ USER_HAS_SUPPORTED, UPVOTING, DOWNVOTING, SUPPORTING_COUNT, DATA_CREATED, DATA_MODIFIED,\ ANSWER_URL, OPPOSING_COUNT, BURYING_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],data['question_id'],data['author']['ukey'],data['content'],data['html'],data['current_user_has_supported'],data['pollings_count'],data['replies_count'],data['supportings_count'],data['date_created'],data['date_modified'],data['url'],data['opposings_count'],data['buryings_count']))

def insertUSER_PROFILE(cursor,data):
    cursor.execute("SELECT USER_ID FROM USER_PROFILE WHERE USER_ID = %s" % data['ukey'])
    results = cursor.fetchall()
  
    if len(results)==0:
        cursor.execute("INSERT INTO USER_PROFILE (USER_ID, NICKNAME, GENDER, CITY, AREA, INTRODUCTION, MASTER_INTRODUCTION, QUESTION_COUNT, ANSWER_COUNT, ANSWER_SUPPORT_COUNT, FOLLOWER_COUNT, FOLLOWING_COUNT, ACTIVITY_COUNT, POST_COUNT, DATE_CREATED, USER_URL, RESOURCE_URL, BADGE_COPPER, BADGE_SILVER, BADGE_GOLD, BADGE_TOTAL, EVENT_VIDEO, TITLE_AUTHORIED, MASTER_CATEGORY, AMENDED_RELIABILITY, TITLE, BLOG_TITLE, TAGGING, BLOG_COUNT, BLOG_URL, BASKET_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['ukey'],data['nickname'],data['gender'],data['city'],data['area'],data['introduction'],data['master_introduction'],data['questions_count'],data['answers_count'],data['answer_supports_count'],data['followers_count'],data['followings_count'],data['activities_count'],data['posts_count'],data['date_created'],data['url'],data['resource_url'],data['badge_counts']['copper'],data['badge_counts']['silver'],data['badge_counts']['gold'],data['badge_counts']['total'],data['event_videos_count'],data['is_title_authorized'],data['master_category'],data['amended_reliability'],data['title'],data['blog_title'],data['taggings'],data['blogs_count'],data['blog_url'],data['baskets_count']))



def insertAnswer_support(cursor,data):
    cursor.execute("SELECT A.ANSWER_ID FROM ANSWER_SUPPORT WHERE ANSWER_ID = %s AND USER_ID = %s"% (data['answer_id'],data['user_polling']['ukey']))
    results = cursor.fetchall()
  
    if len(results)==0:
      cursor.execute("INSERT INTO ANSWER_SUPPORT (USER_ID, ANSWER_ID, QUESTION_ID, DATA_CREATED, OPINION) VALUES(%s,%s,%s,%s,%s);" % (data['user_polling']['ukey'],data['answer_id'],data[''],data['date_created'],data['opinion']))
	

# def insertAnswer(cursor,data):
#     cursor.execute("INSERT INTO ANSWER (ANSWER_ID, QUESTION_ID, USER_ID, CONTENT, ANSWER_HTML, USER_HAS_SUPPORTED, UPVOTING, DOWNVOTING, SUPPORTING_COUNT, DATA_CREATED, DATA_MODIFIED, ANSWER_URL, OPPOSING_COUNT, BURYING_COUNT) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{})". format(data['id'],data['question_id'],data['author']['ukey'],data['content'],data['html'],data['current_user_has_supported'],data['pollings_count'],data['replies_count'],data['supportings_count'],data['date_created'],data['date_modified'],data['url'],data['opposings_count'],data['buryings_count']))


# def insertAnswer_support(cursor,data):
#     cursor.execute("INSERT INTO ANSWER_SUPPORT (USER_ID, ANSWER_ID, QUESTION_ID, DATA_CREATED, OPINION) VALUES({},{},{},{},{})". format(data['user_polling']['ukey'],data['answer_id'],data[''],data['date_created'],data['opinion']))



# def insertTag(cursor,data):
#     cursor.execute("INSERT INTO TAG (QUSETION_ID, TAG_NAME, SUMMARY, QUESTION_COUNT, FOLLOWER_COUNT, DATA_CREATED, DATA_MODIFIED, TAG_URL) VALUES({},{},{},{},{},{},{},{})". format(data['id'],data['tags']['name'],data['tags']['summary'],data['tags']['questions_count'],data['tags']['followers_count'],data['tags']['date_created'],data['tags']['date_modified'],data['tags']['url']))

# def insertUSER_PROFILE(cursor,data):
#     cursor.execute("INSERT INTO USER_PROFILE (USER_ID, NICKNAME, GENDER, CITY, AREA, INTRODUCTION, MASTER_INTRODUCTION, QUESTION_COUNT, ANSWER_COUNT, ANSWER_SUPPORT_COUNT, FOLLOWER_COUNT, FOLLOWING_COUNT, ACTIVITY_COUNT, POST_COUNT, DATE_CREATED, USER_URL, RESOURCE_URL, BADGE_COPPER, BADGE_SILVER, BADGE_GOLD, BADGE_TOTAL, EVENT_VIDEO, TITLE_AUTHORIED, MASTER_CATEGORY, AMENDED_RELIABILITY, TITLE, BLOG_TITLE, TAGGING, BLOG_COUNT, BLOG_URL, BASKET_COUNT) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})". format(data['ukey'],data['nickname'],data['gender'],data['city'],data['area'],data['introduction'],data['master_introduction'],data['questions_count'],data['answers_count'],data['answer_supports_count'],data['followers_count'],data['followings_count'],data['activities_count'],data['posts_count'],data['date_created'],data['url'],data['resource_url'],data['badge_counts']['copper'],data['badge_counts']['silver'],data['badge_counts']['gold'],data['badge_counts']['total'],data['event_videos_count'],data['is_title_authorized'],data['master_category'],data['amended_reliability'],data['title'],data['blog_title'],data['taggings'],data['blogs_count'],data['blog_url'],data['baskets_count']))




with open('question.json', 'r') as data_file:
  data = json.load(data_file)

data['author'] = data['author']['ukey']
data['tags'] = ','.join([x['name'] for x in data['tags']])


for key,value in data.iteritems():
  # print key, ":",type(value)
  if type(value) == type(u''):
    data[key] = value.decode('utf-8')
  data[key] = '\''+str(value)+'\''
    


# print "INSERT INTO QUESTION (QUESTION_ID,USER_ID, QUESTION, SUMMARY, ANSWER_COUNT, FOLLOWER_COUNT,ARCHIVE_COUNT, DATA_CREATED, DATA_LAST_ANSWERED, QUESTION_URL,REPLY_COUNT, RECOMMEND_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],data['author'],data['question'],data['summary'],data['answers_count'],data['followers_count'],data['archives_count'],data['date_created'],data['date_last_answered'],data['url'],data['replies_count'],data['recommends_count'])



mariadb_connection = mariadb.connect(user='ming', password = '', database='cqavoting')

cursor = mariadb_connection.cursor()

# insertQuestion(cursor,data)

# mariadb_connection.commit()

cursor.execute("select * from ANSWER_SUPPORT;")
results = cursor.fetchall()

for x in range(len(results)):
  print results

# f = open('IST343.sql','r')
# query = "".join(f.readlines())
# cursor.execute(query,multi = True)
# res = cursor.execute('show databases;')
# print(res)
# f.close()
# cursor.execute("INSERT INTO test (ID, MSG) values({},{})".format(1,"\"学习学习\""))
# cursor.execute("INSERT INTO test (ID, MSG) values({},{})".format(2,"\"常识\""))

# ID = 2
# cursor.execute("select ID from test where ID = " + str(ID)+";")
# results = cursor.fetchall()
# print len(results)


cursor.close()
mariadb_connection.close()
