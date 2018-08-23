import os

folder = '/Users/Colin/skysunwei/blog'

urls = []
file_names = []

for root, dirs, files in os.walk(folder):
    for file in files:
        file_names.append(file.strip('.html'))
        # print file

blogs = {}
blog_name = ''
blog_time = ''

for line in open('data'):
    line = line.strip(' ').strip('\t').strip('\n')

    if '/4855115/posts' in line and 'quick_verify' not in line:
        temp1 = line.split('<a href=\"')
        temp2 = temp1[1].split('\" title=')
        temp3 = temp2[1].split('\">')
        blog_name = temp3[1].strip('</a>')

    if '<td class="last-col">20' in line:
        blog_time = line.strip("</td>").replace("class=\"last-col\">", '')

    if blog_name is not '' and blog_time is not '':
        blogs[blog_name] = blog_time


blogs = sorted(blogs.items(),key = lambda x:x[1],reverse = True)


for key in blogs:

    if str(key[0]) in file_names:
        urls.append('%s\t<a href=\"blog\%s.html\">%s</a><br><br>' % (key[1], key[0], key[0]))
    else:
        print key[0]

for url in urls:
    print url

print len(urls)