from io import BytesIO, StringIO

nio = StringIO("wudinggao")
print(nio.write("hahahaha"))
print(nio.write("haha"))
print(nio.getvalue())
nio = BytesIO(b"wudinggao")
print(nio.read().decode())
