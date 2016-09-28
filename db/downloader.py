import requests # for retriving json data
import json # for parse json (not used for nwo)
import random # for randomly select proxy and user agent
import grey_harvest # for scrape available proxies





''' spawn a harvester '''
harvester = grey_harvest.GreyHarvester()

''' harvest some proxies from teh interwebz '''

'''
    each proxy item has following format: {'ip': '88.191.174.188', 'https': True, 'port': 80, 'latency': 9045, 'country': 'France'}
'''

print "searching for good proxies ip addresses..."

proxies_list = []

number_of_proxy = 2
count = 0
for proxy in harvester.run():
    if proxy['https']:
        proxies_list.append(proxy)
        count += 1
        if count >=number_of_proxy:
                break


# print proxies_list

#####
# Proxy format:
# http://<USERNAME>:<PASSWORD>@<IP-ADDR>:<PORT>
#####


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

random_proxy = random.choice(proxies_list)


proxy = {
    "http": "http://"+random_proxy['ip']+":"+str(random_proxy['port']),
}

# load user agents and set headers
uas = LoadUserAgents()
ua = random.choice(uas)  # select a random user agent
headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

# make the request

# now make the request
url = 'http://apis.guokr.com/ask/question.json?retrieve_type=by_tag&tag_name=%E6%88%91%E5%A5%BD%E6%83%B3%E9%97%AE&limit=20'
r = requests.get(url, proxies=proxy,headers=headers)


try:
    if r.status_code == 200:
        jsonStr = json.dumps(r.json(), encoding='gbk', ensure_ascii=False).encode('gbk')
        print jsonStr
except ValueError as e:
    print e 


