domain = 'http://blog.home.blogbus.com'

urls = []

for line in open('data'):
    line = line.strip(' ').strip('\t').strip('\n')
    if '/4855115/posts' in line and 'quick_verify' not in line:
        temp1 = line.split('<a href=\"')
        temp2 = temp1[1].split('\" title=')
        temp3 = temp2[1].split('\">')

        urls.append('<a href=\"%s\">%s</a><br><br>' % (domain + temp2[0], temp3[1].strip('</a>')))
        # print temp2[0]

for url in urls:
    print url

