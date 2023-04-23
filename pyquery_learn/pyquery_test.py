import urllib

from lxml import etree
from pyquery import PyQuery as pq

d = pq("<html></html>")
print(d)
d = pq(etree.fromstring("<html></html>"))
print(d)
d = pq(url="http://google.com/")
print(d)
