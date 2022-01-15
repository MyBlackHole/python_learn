from lxml import etree
from bs4 import BeautifulSoup

with open('1.html', 'r', encoding='utf8') as f:
    text = f.read()

soup = BeautifulSoup(text, "html5lib")
# print(soup.prettify())
html = etree.HTML(soup.prettify())

card = html.xpath('//div[@class="card-wrap"]')
print(etree.tostring(card[0], encoding='utf8').decode())
