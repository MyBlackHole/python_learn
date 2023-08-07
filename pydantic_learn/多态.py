from typing import Dict, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class SshUser(User):
    ssh_name: str


class AgentUser(User):
    agent_name: str


class Info(BaseModel):
    user: Union[SshUser, AgentUser, Dict]


if __name__ == "__main__":
    info_dict = {
        "user": {
            "id": 123,
            "name": "research",
            # "ssh_name": "research",
            "agent_name": "research",
        }
    }

    info = Info(**info_dict)
    print(info)

    ssh_user_dict = {
        "id": 123,
        "name": "research",
        "ssh_name": "research",
    }
    ssh_user = SshUser(**ssh_user_dict)
    print(ssh_user)

    print(SshUser(id=1, name="1", ssh_name="2").dict())
