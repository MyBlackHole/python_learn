import hashlib
import hmac

import cryptography.fernet

x = hashlib.blake2b()
x.update(b"asd")
print("x = " + x.hexdigest())
print(
    "true"
    if hmac.compare_digest(x.hexdigest(), hashlib.blake2b(b"asd").hexdigest())
    else "false"
)

y = hashlib.blake2b(digest_size=5, key=b"", salt=b"", person=b"")  # 键控哈希、加盐、个性化
y.update(b"asd")
print("y = " + y.hexdigest())
print(
    "true"
    if hmac.compare_digest(
        y.hexdigest(),
        hashlib.blake2b(
            b"asd", digest_size=5, key=b"", salt=b"", person=b""
        ).hexdigest(),
    )
    else "false"
)

a = cryptography.fernet.Fernet.generate_key()  # 自动生成密钥
b = cryptography.fernet.Fernet(a)
c = b.encrypt("asd".encode())  # 使用生成的密钥加密
print(c)
d = b.decrypt(c)  # 使用生成的密钥解密
print(d.decode())

z = hmac.new(a, digestmod=hashlib.blake2b)  # 使用本地密钥进行加密
z.update(b"asd")
print("z = " + z.hexdigest())
print(
    "true"
    if hmac.compare_digest(
        z.hexdigest(),
        hmac.new(key=a, msg=b"asd", digestmod=hashlib.blake2b).hexdigest(),
    )
    else "false"
)

