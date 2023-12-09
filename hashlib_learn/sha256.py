import hashlib

x = hashlib.sha256()
x.update(b"asd")
print("x_1 = " + x.hexdigest())

x = hashlib.sha256()
x.update("asd".encode())
print("x_2 = " + x.hexdigest())

x = hashlib.sha256()
x.update(b"a")
x.update(b"s")
x.update(b"d")
print("x_3 = " + x.hexdigest())

y = hashlib.sha256(b"asd").hexdigest()
print("y_1 = " + y)

z = hashlib.new("sha256")
z.update(b"asd")
print("z_1 = " + z.hexdigest())
