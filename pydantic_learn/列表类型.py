from datetime import datetime
from typing import List

from pydantic import BaseModel, parse_obj_as, validator, field_serializer


class User(BaseModel):
    name: str
    age: int

    data: datetime

    @field_serializer("data", pre=True)
    def parse_data(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d %H:%M:%S"
        ).date()


users = [
    {
        "name": "user1",
        "age": 15,
        "data": datetime.now(),
    },
    {
        "name": "user2",
        "age": 28,
        "data": datetime.now(),
    },
]

m = parse_obj_as(List[User], users)
print(m)
print(m[0].dict())
