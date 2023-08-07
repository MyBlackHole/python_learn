from datetime import date
from enum import Enum
from typing import List, Union

from pydantic import BaseModel


class Gender(str, Enum):
    man = "man"
    women = "women"


class Person(BaseModel):
    name: str
    gender: Gender


class Department(BaseModel):
    name: str
    lead: Person
    cast: List[Person]


class Group(BaseModel):
    owner: Person
    member_list: List[Person] = []


class Company(BaseModel):
    name: str
    owner: Union[Person, Group]
    regtime: date
    department_list: List[Department] = []


if __name__ == "__main__":
    sales_department = {
        "name": "sales",
        "lead": {"name": "Sarah", "gender": "women"},
        "cast": [
            {"name": "Sarah", "gender": "women"},
            {"name": "Bob", "gender": "man"},
            {"name": "Mary", "gender": "women"},
        ],
    }

    research_department = {
        "name": "research",
        "lead": {"name": "Allen", "gender": "man"},
        "cast": [
            {"name": "Jane", "gender": "women"},
            {"name": "Tim", "gender": "man"},
        ],
    }

    company = {
        "name": "Fantasy",
        "owner": {"name": "Victor", "gender": "man"},
        "regtime": "2020-7-23",
        "department_list": [sales_department, research_department],
    }

    company = Company(**company)
    import pdb
    pdb.set_trace()
    print(company.json())
