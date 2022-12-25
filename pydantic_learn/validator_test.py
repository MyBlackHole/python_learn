import re

from pydantic import BaseModel, validator


class Password(BaseModel):
    password: str

    @validator("password")
    def password_rule(cls, password):
        def is_valid(password):
            if len(password) < 6 or len(password) > 20:
                return False
            if not re.search("[a-z]", password):
                return False
            if not re.search("[A-Z]", password):
                return False
            if not re.search(r"\d", password):
                return False
            return True

        if not is_valid(password):
            raise ValueError("password is invalid")
