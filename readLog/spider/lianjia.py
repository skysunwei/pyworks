import requests
from BeautifulSoup import BeautifulSoup

pages = range(1, 1000)
xiaoqus = ['dongcheng','xicheng','chaoyang','fengtai','shijingshan','tongzhou','changping','daxing','yizhuangkaifaqu','shunyi','fangshan','mentougou','pinggu','huairou','miyun','yanqing']

lines = []

for xq in xiaoqus:

    exist = 0

    for page in pages:

        print xq, page

        if exist is 1:
            break

        url = "https://m.lianjia.com/bj/xiaoqu/%s/pg%s/?_t=1" % (xq, page)
        ret = requests.get(url)

        if ret.status_code == 200:
            soup = BeautifulSoup(ret.text)

            # print soup
            for div in soup.findAll(name='div', attrs={"class":"item_main"}):
                # print div
                # print div.string
                try:
                    data = str(div.string) + '\n'
                    if data in lines:
                        exist = 1
                    else:
                        lines.append(data)
                except:
                    # print div.string
                    continue
                # lines.append(div.string)
        else:
            print ret.status_code
            break

datas = list(set(lines))
print len(datas)

# exit()

distrit_file = 'districts.txt'
f = file(distrit_file, "w+")
for data in datas:
    f.writelines(data)
f.close()

print 'done'



