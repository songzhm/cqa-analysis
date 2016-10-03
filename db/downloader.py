import requests # for retriving json data
import json # for parse json (not used for nwo)
import random # for randomly select proxy and user agent
import grey_harvest # for scrape available proxies
import time

def get_url_data(url,headers,proxy):
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=1)
    sess.mount('http://', adapter)
    try:
        print "retriving data using proxy", proxy
        r = sess.get(url, proxies=proxy,headers=headers)
        if r.status_code == 200:
            print "get the data back, storing it ..."

            return r.json()

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print "Failed, retry after 3 seconds ... "
        time.sleep(3)
        return get_url_data(url,headers,proxy)





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


''' spawn a harvester '''
harvester = grey_harvest.GreyHarvester()

''' harvest some proxies from teh interwebz '''

print "searching for good proxies ip addresses..."


number_of_proxy = 100
count = 0

proxies_list=[]

for proxy in harvester.run():
    if proxy['https']:
        
        proxies_list.append(proxy)

        # proxy_requests = {
        #     "http": "http://"+proxy['ip']+":"+str(proxy['port']),
        # }
        # # load user agents and set headers
        # uas = LoadUserAgents()
        # ua = random.choice(uas)  # select a random user agent
        # headers = {
        #     "Connection" : "close",  # another way to cover tracks
        #     "User-Agent" : ua}


        # # now make the request
        # url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name=%E6%88%91%E5%A5%BD%E6%83%B3%E9%97%AE&limit=5&offset='+str(4*count)
        # res = get_url_data(url,headers,proxy_requests)
        
        # with open(str(count+1)+'data.json', 'w') as fp:
        #     json.dump(res, fp)

        # # try:
        # #     r = sess.get(url, proxies=proxy_requests,headers=headers)
        # #     if r.status_code == 200:
        # #         jsonStr = json.dumps(r.json(), encoding='gbk', ensure_ascii=False).encode('gbk')
        # #         print jsonStr

        # #         count+=1

        # # except requests.exceptions.RequestException as e:  # This is the correct syntax
        # #     print e
        # #     print "getting data failed! getting a new proxy address ... "
        # # for tick in range(5):
        # #     print "sleeping" + str(5-tick)
        # #     time.sleep(1)
        count+=1
        print(count)
    if count> number_of_proxy:
        break

print(proxies_list)


