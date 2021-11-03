from pyquery import PyQuery as pq
from lxml import etree
import urllib

d = pq("<html></html>")
print(d)
d = pq(etree.fromstring("<html></html>"))
print(d)
d = pq(url='http://google.com/')
print(d)
