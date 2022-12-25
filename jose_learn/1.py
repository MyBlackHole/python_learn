from jose import jwt

token = jwt.encode({"key": "value"}, "secret", algorithm="HS256")
print(token)

print(jwt.decode(token, "secret", algorithms=["HS256"]))
