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


# from typing import Dict, Union

# from pydantic import BaseModel


# class Data(BaseModel):
#     data: str
#     pass


# class Log(BaseModel):
#     log: str
#     pass


# class Backup(BaseModel):
#     pass


# class MySQLBackup(Backup):
#     mysql: str
#     op: Union[Data, Log]
#     # data_backup = Data
#     # log_backup = Log


# class TdsqlUser(MySQLBackup):
#     tdsql: str


# class Info(BaseModel):
#     op: Union[MySQLBackup, TdsqlUser, Dict]


# # class User(BaseModel):
# #     id: int
# #     name: str
# #
# #
# # class SshUser(User):
# #     ssh_name: str
# #
# #
# # class AgentUser(User):
# #     agent_name: str
# #
# #
# # class Info(BaseModel):
# #     user: Union[SshUser, AgentUser, Dict]
# if __name__ == "__main__":
#     info_dict = {
#         "op": {
#             "mysql": "type",
#             "op": {
#                 "log": "type_1",
#             },
#         }
#     }
#     info = Info(**info_dict)
#     print(info)
#     # ssh_user_dict = {
#     #     "id": 123,
#     #     "name": "research",
#     #     "ssh_name": "research",
#     # }
#     # ssh_user = SshUser(**ssh_user_dict)
#     # print(ssh_user)
#     # print(SshUser(id=1, name="1", ssh_name="2").dict())
