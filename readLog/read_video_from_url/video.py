import requests
from BeautifulSoup import BeautifulSoup

url = 'http://v.qq.com/page/k/f/k/k0302a3rmfk.html?ptag=v.qq.com%23v.play.adaptor%232&mreferrer=http%3A%2F%2Fv.qq.com%2Fu%2Fvideos%2F'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text).find('item_main')
    print soup
    print soup['src']
else:
    print page.status_codeF
