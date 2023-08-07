from typing import Dict, Union

from sqlmodel import SQLModel


class User(SQLModel):
    id: int
    name: str


class SshUser(User):
    ssh_name: str

    def connc():
        pass

class AgentUser(User):
    agent_name: str

    def connc():
        pass


class Info(SQLModel):
    user: Union[SshUser, AgentUser, Dict]


if __name__ == "__main__":
    info_dict = {
        "user": {
            "name": "research",
            "ssh_name": "research",
            # "agent_name": "research",
        }
    }

    info = Info(**info_dict)
    print(info.dict())
    # print(info.dict(exclude_none=True))

    # ssh_user_dict = {
    #     "id": 123,
    #     "name": "research",
    #     "ssh_name": "research",
    # }
    # # ssh_user = SshUser(**ssh_user_dict)
    # ssh_user = SshUser.parse_obj(ssh_user_dict)
    # print(ssh_user)

    # print(SshUser(id=1, name="1", ssh_name="2").dict())
