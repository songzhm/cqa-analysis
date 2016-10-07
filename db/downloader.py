# -*- coding: utf-8 -*-


import requests # for retriving json data
import json # for parse json (not used for nwo)
import random # for randomly select proxy and user agent
# import grey_harvest # for scrape available proxies
import time
from pprint import pprint
from pymongo import MongoClient



def get_url_data(url,headers,proxies_list):
    proxy = random.choice(proxies_list)

    proxy_requests = {
        "http": "http://"+proxy['ip']+":"+str(proxy['port']),
    }
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=1)
    sess.mount('http://', adapter)
    try:
        print "retriving data using proxy", proxy_requests
        r = sess.get(url, proxies=proxy_requests,headers=headers,timeout=15)
        if r.status_code == 200:
            print "get the data back, storing it ..."

            return r.json()
        else:
            raise Exception

    except Exception as e:  # This is the correct syntax
        print e
        time.sleep(2)
        return get_url_data(url,headers,proxies_list)



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


thefile = open('proxies.json','r')
proxies_list=json.load(thefile)
thefile.close()
print(proxies_list)


# proxy = random.choice(proxies_list)

# proxy_requests = {
#     "http": "http://"+proxy['ip']+":"+str(proxy['port']),
# }
# load user agents and set headers
uas = LoadUserAgents()
ua = random.choice(uas)  # select a random user agent
headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

tags = [u'健康'.encode('utf-8')]
totals = [10977]


# %E6%88%91%E5%A5%BD%E6%83%B3%E9%97%AE

LIMIT = 100

# now make the request
# url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name='+tags[0]+'&limit=5&offset=0'
# res = get_url_data(url,headers,proxy_requests)
# pprint(res['total'])
# with open(str(count+1)+'data.json', 'w') as fp:
#     json.dump(res, fp)
client = MongoClient()
db = client.test
for count in range(len(tags)):
    tag = tags[count]
    total = totals[count]
    for offset_ind in range((total/LIMIT + 1)):
        url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name='+tag+'&limit='+str(LIMIT)+'&offset='+str(LIMIT*offset_ind)
        res = get_url_data(url,headers,proxies_list)
        data = res['result']
        response = db.questionByTag.insert_many(data)
        print 'items retrived and stored:' + str(db.questionByTag.count())
        print 'items left: ' + str(total - db.questionByTag.count())
    
        for s in range(3):
            print 'break: '+ str(3-s)
            time.sleep(1) 



