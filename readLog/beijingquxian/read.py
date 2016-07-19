#-*- coding: UTF-8 -*-

import json
import requests

url = 'http://d.jd.com/area/get?fid='

page = requests.get(url + '1')

if page.status_code == 200:

    beijing_districts = json.loads(page.text)

    for district in beijing_districts:
        print district['name']

        district_page = requests.get(url + str(district['id']))
        areas = json.loads(district_page.text)

        for area in areas:
            print area['name']

        print
else:
    print page.status_code


# insert `district`(`title`,`level`,`usetype`,`parentid`,`deleted`) values('xxx',3,3,1,0);