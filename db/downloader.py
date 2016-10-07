# -*- coding: utf-8 -*-


import requests # for retriving json data
import json # for parse json (not used for nwo)
import random # for randomly select proxy and user agent
# import grey_harvest # for scrape available proxies
import time
from pprint import pprint
from pymongo import MongoClient


def LoadUserAgents(uafile='user_agents.txt'):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas


# load user agents and set headers
uas = LoadUserAgents()

# ua = random.choice(uas)  # select a random user agent
# headers = {
#     "Connection" : "close",  # another way to cover tracks
#     "User-Agent" : ua}


def get_new_header(uas):
    ua = random.choice(uas)
    return {"Connection" : "close", "User-Agent" : ua}


thefile = open('proxies.json','r')
proxies_list=json.load(thefile)
thefile.close()
# print(proxies_list)


# proxy = random.choice(proxies_list)

# proxy_requests = {
#     "http": "http://"+proxy['ip']+":"+str(proxy['port']),
# }


def get_url_data(url,use_proxy=True):
    global uas
    global proxies_list
    if use_proxy:
        proxy = random.choice(proxies_list)

        proxy_requests = {
            "http": "http://"+proxy['ip']+":"+str(proxy['port']),
        }

        headers = get_new_header(uas)

        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=1)
        sess.mount('http://', adapter)
        try:
            print "retriving data using proxy", proxy_requests #, "and header", headers
            # r = sess.get(url, proxies=proxy_requests,headers=headers,timeout=15)
            r = sess.get(url, proxies=proxy_requests,timeout=15)
            if r.status_code == 200:
                # print "get the data back, storing it ..."

                return r.json()
            else:
                raise Exception

        except Exception as e:  # This is the correct syntax
            print e
            print 're-try with new ip ...'
            time.sleep(2)
            return get_url_data(url,use_proxy)
    else:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=1)
        sess.mount('http://', adapter)
        try:
            print "retriving data using default ip"
            # r = sess.get(url, proxies=proxy_requests,headers=headers,timeout=15)
            r = sess.get(url,timeout=15)
            if r.status_code == 200:
                # print "get the data back, storing it ..."

                return r.json()
            else:
                raise Exception

        except Exception as e:  # This is the correct syntax
            print e
            print 're-try ...'
            time.sleep(2)
            return get_url_data(url,uas,proxies_list)
        





# ''' spawn a harvester '''
# harvester = grey_harvest.GreyHarvester()

# ''' harvest some proxies from teh interwebz '''

# print "searching for good proxies ip addresses..."


# number_of_proxy = 100
# count = 0

# proxies_list=[]

# for proxy in harvester.run():
#     if proxy['https']:
        
#         proxies_list.append(proxy)


#         count+=1
#         print(count)
#     if count> number_of_proxy:
#         break


# thefile = open('proxies.txt','w')
# for item in proxies_list:
#   thefile.write("%s\n" % item)

# thefile.close()



    
# tag: health
chinese_tags = [u'生活']

tags = [x.encode('utf-8') for x in chinese_tags]


# %E6%88%91%E5%A5%BD%E6%83%B3%E9%97%AE

LIMIT = 200

# now make the request
# url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name='+tags[0]+'&limit=5&offset=0'
# res = get_url_data(url,headers,proxy_requests)
# pprint(res['total'])
# with open(str(count+1)+'data.json', 'w') as fp:
#     json.dump(res, fp)
client = MongoClient()
db = client.test
usring_proxy = False
for count in range(len(tags)):
    tag = tags[count]
    print 'getting total question numbers under current tag...'
    url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name='+tag+'&limit=1&offset=0'
    res = get_url_data(url,usring_proxy)
    total = res['total']
    print total, 'questions under current tag...'
    sleep_time = 5
    for offset_ind in range((total/LIMIT + 1)):
        url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name='+tag+'&limit='+str(LIMIT)+'&offset='+str(LIMIT*offset_ind)
        res = get_url_data(url,usring_proxy)
        question_list = res['result']
        if len(question_list)>0:
            
            response = db.questionByTag.insert_many(question_list)
            print 'items retrived and stored:' + str(db.questionByTag.count())
            print 'items left: ' + str(total - db.questionByTag.count())
            print 'retriving answers data now...'
            
            for question in question_list:
                
                q_id = question['id']
                print 'getting total answer numbers under current question:',str(q_id)
                url = 'http://apis.guokr.com/ask/answer.json?retrieve_type=by_question&question_id='+str(q_id)+'&limit=1&offset=0'
                res = get_url_data(url,usring_proxy)
                q_total = res['total']
                print 'total answers:', q_total
                
                q_sleep_time = 3
                for q_offset_ind in range((q_total/LIMIT + 1)):
                    url = 'http://apis.guokr.com/ask/answer.json?retrieve_type=by_question&question_id='+str(q_id)+'&limit='+str(LIMIT)+'&offset='+str(LIMIT*q_offset_ind)
                    res = get_url_data(url,usring_proxy)
                    answer_list = res['result']
                    if len(answer_list)>0:
                        response = db.answerByQuestion.insert_many(answer_list)
                        print 'items retrived and stored:' + str(len(response.inserted_ids))
                        print 'items left: ' + str(q_total - len(response.inserted_ids))
                    else:
                        print 'answer list is empty!'
                        
                        
                    for s in range(q_sleep_time):
                        print 'break: '+ str(q_sleep_time-s)
                        time.sleep(1) 
        else:
            print 'question list is empty!'



    
        for s in range(sleep_time):
            print 'break: '+ str(sleep_time-s)
            time.sleep(1) 



