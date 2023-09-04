import json
from pydantic import BaseModel
from pydantic.json import pydantic_encoder


class A(BaseModel):
    a: str

print(A(a="2"))
As = [A(a="2"), A(a="3"), A(a="4")]
print(As)
print(json.dumps(As, default=pydantic_encoder))
