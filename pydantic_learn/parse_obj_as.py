from typing import Union
from pydantic import BaseModel, parse_obj_as


class A(BaseModel):
    a: str


class B(BaseModel):
    b: str


info = {
    # "a": 1,
    "b": 1,
}


m = parse_obj_as(Union[A, B], info)
print(m, type(m))
