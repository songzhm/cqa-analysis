import requests # for retriving json data
import json # for parse json (not used for nwo)
import random # for randomly select proxy and user agent
import gray_harvest # for scrape available proxies

def LoadUserAgents(uafile='db/user_agents.txt'):
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
count = 0
for proxy in harvester.run():
        print(proxy)
        count += 1
        if count >= 20:
                break


#####
# Proxy format:
# http://<USERNAME>:<PASSWORD>@<IP-ADDR>:<PORT>
#####
proxy = {
    "http": "http://97.77.104.22:80",
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
        
        print(r.json())
except ValueError as e:
    print(e)