
import mysql.connector as mariadb

class MariaDB():
    def __init__(self,username, password, dbname):
        self.mariadb_connection = mariadb.connect(user=str(username), password = str(password), database=str(dbname))
        self.cursor = self.mariadb_connection.cursor()
    
    def insertQuestion(self, data):
        data = self.transform_data(data)
        self.cursor.execute("SELECT QUESTION_ID FROM QUESTION WHERE QUESTION_ID = %s ;" % (data['id']))
        results = self.cursor.fetchall()

        if len(results)==0:
            self.cursor.execute("INSERT INTO QUESTION (QUESTION_ID,USER_ID, QUSETION, SUMMARY, ANSWER_COUNT,\
            FOLLOWER_COUNT,ARCHIVE_COUNT, DATA_CREATED, DATA_LAST_ANSWERED, QUESTION_URL,REPLY_COUNT,\
            RECOMMEND_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],'\'' + data['author']['ukey']+'\'',\
            data['question'],data['summary'],data['answers_count'],data['followers_count'],\
            data['archives_count'],data['date_created'],data['date_last_answered'],data['url'],\
            data['replies_count'],data['recommends_count']))
            
            self.mariadb_connection.commit()
        
    def insertTag(self,data):
        data = self.transform_data(data)
        self.cursor.execute("SELECT TAG_NAME FROM TAG WHERE TAG_NAME = %s ;" % (data['name']))

        results = self.cursor.fetchall()

        if len(results)==0:
            self.cursor.execute("INSERT INTO TAG (TAG_NAME,SUMMARY,QUESTION_COUNT,FOLLOWER_COUNT, DATE_CREATED,DATE_MODIFIED,TAG_URL) \
            VALUES(%s,%s,%s,%s,%s,%s,%s);" % (data['name'],data['summary'],'\''+str(data['questions_count'])+'\'','\''+str(data['followers_count'])+'\'',data['date_created'],data['date_modified'],data['url']))
            
            self.mariadb_connection.commit()

    def insertQuestion_Tag(self,data):
        data = self.transform_data(data)
        self.cursor.execute("SELECT ID FROM QUESTION_TAG WHERE QUESTION_ID = %s AND TAG_NAME = %s ;" % (data['question_id'],data['tag_name']))
        
        results = self.cursor.fetchall()

        if len(results)==0:
            self.cursor.execute("INSERT INTO QUESTION_TAG (QUESTION_ID, TAG_NAME) VALUES(%s, %s) ;" % (data['question_id'], data['tag_name']))
        
            self.mariadb_connection.commit()
        

    def insertAnswer(self,data):
        data = self.transform_data(data)
        self.cursor.execute("SELECT ANSWER_ID FROM ANSWER WHERE ANSWER_ID = %s ;" % (data['id']))
        results = self.cursor.fetchall()
        
        if len(results)==0:
            # print "INSERT INTO ANSWER (ANSWER_ID, QUESTION_ID, USER_ID, CONTENT, ANSWER_HTML,USER_HAS_SUPPORTED, UPVOTING, DOWNVOTING, SUPPORTING_COUNT, DATA_CREATED, DATA_MODIFIED, ANSWER_URL, OPPOSING_COUNT, BURYING_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],data['question_id'],'\''+data['author']['ukey']+'\'',data['content'],data['html'],data['current_user_has_supported'],data['pollings_count'],data['replies_count'],data['supportings_count'],data['date_created'],data['date_modified'],data['url'],data['opposings_count'],data['buryings_count'])

            self.cursor.execute("INSERT INTO ANSWER (ANSWER_ID, QUESTION_ID, USER_ID, CONTENT, ANSWER_HTML,USER_HAS_SUPPORTED, UPVOTING, DOWNVOTING, SUPPORTING_COUNT, DATA_CREATED, DATA_MODIFIED, ANSWER_URL, OPPOSING_COUNT, BURYING_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['id'],data['question_id'],'\''+data['author']['ukey']+'\'',data['content'],data['html'],data['current_user_has_supported'],data['pollings_count'],data['replies_count'],data['supportings_count'],data['date_created'],data['date_modified'],data['url'],data['opposings_count'],data['buryings_count']))
            
            self.mariadb_connection.commit()


    def insertUSER_PROFILE(self,data):
        data = self.transform_data(data)
        data['taggings'] = '\''+ 'NULL' + '\''# '\'' +str(data['taggings'])+'\''
        self.cursor.execute("SELECT USER_ID FROM USER_PROFILE WHERE USER_ID = %s ;" % data['ukey'])
        results = self.cursor.fetchall()
    
        if len(results)==0:
            # print "INSERT INTO USER_PROFILE (USER_ID, NICKNAME, GENDER, CITY, AREA, INTRODUCTION, MASTER_INTRODUCTION, QUESTION_COUNT, ANSWER_COUNT, ANSWER_SUPPORT_COUNT, FOLLOWER_COUNT, FOLLOWING_COUNT, ACTIVITY_COUNT, POST_COUNT, DATE_CREATED, USER_URL, RESOURCE_URL, BADGE_COPPER, BADGE_SILVER, BADGE_GOLD, BADGE_TOTAL, EVENT_VIDEO, TITLE_AUTHORIED, MASTER_CATEGORY, AMENDED_RELIABILITY, TITLE, BLOG_TITLE, TAGGING, BLOG_COUNT, BLOG_URL, BASKET_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['ukey'],data['nickname'],data['gender'],data['city'],data['area'],data['introduction'],data['master_introduction'],data['questions_count'],data['answers_count'],data['answer_supports_count'],data['followers_count'],data['followings_count'],data['activities_count'],data['posts_count'],data['date_created'],data['url'],data['resource_url'],data['badge_counts']['copper'],data['badge_counts']['silver'],data['badge_counts']['gold'],data['badge_counts']['total'],data['event_videos_count'],data['is_title_authorized'],data['master_category'],data['amended_reliability'],data['title'],data['blog_title'],data['taggings'],'\''+str(data['blogs_count'])+'\'',data['blog_url'],data['baskets_count'])

            self.cursor.execute("INSERT INTO USER_PROFILE (USER_ID, NICKNAME, GENDER, CITY, AREA, INTRODUCTION, MASTER_INTRODUCTION, QUESTION_COUNT, ANSWER_COUNT, ANSWER_SUPPORT_COUNT, FOLLOWER_COUNT, FOLLOWING_COUNT, ACTIVITY_COUNT, POST_COUNT, DATE_CREATED, USER_URL, RESOURCE_URL, BADGE_COPPER, BADGE_SILVER, BADGE_GOLD, BADGE_TOTAL, EVENT_VIDEO, TITLE_AUTHORIED, MASTER_CATEGORY, AMENDED_RELIABILITY, TITLE, BLOG_TITLE, TAGGING, BLOG_COUNT, BLOG_URL, BASKET_COUNT) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" % (data['ukey'],data['nickname'],data['gender'],data['city'],data['area'],data['introduction'],data['master_introduction'],data['questions_count'],data['answers_count'],data['answer_supports_count'],data['followers_count'],data['followings_count'],data['activities_count'],data['posts_count'],data['date_created'],data['url'],data['resource_url'],data['badge_counts']['copper'],data['badge_counts']['silver'],data['badge_counts']['gold'],data['badge_counts']['total'],data['event_videos_count'],data['is_title_authorized'],data['master_category'],data['amended_reliability'],data['title'],data['blog_title'],data['taggings'],'\''+str(data['blogs_count'])+'\'',data['blog_url'],data['baskets_count']))

            self.mariadb_connection.commit()


    def insertAnswer_support(self,data,question_id):
        data = self.transform_data(data)
        self.cursor.execute("SELECT QUESTION_ID, ANSWER_ID, USER_ID FROM ANSWER_SUPPORT WHERE QUESTION_ID = %s AND ANSWER_ID = %s AND USER_ID = %s ;" % ('\''+str(question_id)+'\'', data['answer_id'],'\''+str(data['user_polling']['ukey'])+'\''))
        results = self.cursor.fetchall()
    
        if len(results)==0:
            self.cursor.execute("INSERT INTO ANSWER_SUPPORT (USER_ID, ANSWER_ID, QUESTION_ID, DATA_CREATED, OPINION) VALUES(%s,%s,%s,%s,%s);" % ('\''+data['user_polling']['ukey']+'\'',data['answer_id'],'\''+str(question_id)+'\'',data['date_created'],data['opinion']))
            
            self.mariadb_connection.commit()

    def select(self,query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results 
    
    def transform_data(self,data):
        for key,value in data.iteritems():
      # print key, ":",type(value)
            if type(value) == type(u''):
                data[key] = value.decode('utf-8')
                data[key] = '\''+ str(value) + '\''
            if data[key] is None:
                data[key] = '\''+ 'NULL' + '\''
            
        return data

    def kill(self):
        self.cursor.close()
        self.mariadb_connection.close()

            