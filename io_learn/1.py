from io import BytesIO
from io import StringIO

nio = StringIO('wudinggao')
print(nio.write('hahahaha'))
print(nio.write('haha'))
print(nio.getvalue())
nio = BytesIO(b'wudinggao')
print(nio.read().decode())
