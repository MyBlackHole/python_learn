from pyquery import PyQuery

with open('1.html', 'r') as f:
    contents = f.read()

doc = PyQuery(contents)
# print(type(doc))
text = doc(".card-wrap")
list1 = []
for i in text.items():
    list1.append(i)

print(list1)
print(type(list1[0]))

# text = doc('card-wrap').html()
# print(text)
