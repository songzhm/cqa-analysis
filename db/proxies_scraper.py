# -*- coding: utf-8 -*-


import grey_harvest # for scrape available proxies
from pprint import pprint
import json

''' spawn a harvester '''
harvester = grey_harvest.GreyHarvester()

''' harvest some proxies from teh interwebz '''

print "searching for good proxies ip addresses..."


number_of_proxy = 150
count = 0

proxies_list=[]

for proxy in harvester.run():
    if proxy['https']:
        
        proxies_list.append(proxy)


        count+=1
        print(count)
    if count> number_of_proxy:
        break

pprint(proxies_list)

thefile = open('proxies.json','w')

json.dump(proxies_list,thefile)
thefile.close()

