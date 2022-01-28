from ssl import OP_NO_RENEGOTIATION
import requests
import re 
from bs4 import BeautifulSoup

req = requests.get('https://www.digikala.com/search/category-mobile-phone/?q=%d8%a7%d9%be%d9%84&entry=mm')

soup = BeautifulSoup(req.text, 'html.parser')
# val = suop.find_all('params')
for link in soup.find_all('a'):
    print(link.get('data-snt-params'))