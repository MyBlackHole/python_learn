from collections import namedtuple

Book = namedtuple("Book", ["name", "price", "count"])

book1 = Book(name="python", price=100, count=10)
print(book1)

# 使用字典赋值
book_dict = {"name": "c++", "price": 99, "count": 10}

book2 = Book(**book_dict)
print(book2)
