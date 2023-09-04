from typing import Dict, Optional, Union

from pydantic import BaseModel


class Data(BaseModel):
    test: str
    data: Optional[str]

    def print_a(self, **kwargs):
        print("{}".format("data"))


class Log(BaseModel):
    log: str

    def print_a(self, **kwargs):
        print("{}".format("log"))


class MySQData(Data):
    pass

class OData(Data):
    pass

class MySQLLog(Log):
    pass


class TdSqlLog(MySQLLog):

    def print_a(self, **kwargs):
        print("{}".format("tdsqllog"))


class ProxyLog(Log):
    proxy_log: str

    def print_a(self, **kwargs):
        print("{}".format("proxylog"))

class ProxyOLog(Log):
    proxy_O_log: str

    def print_a(self, **kwargs):
        print("{}".format("proxylog"))


class Backup(BaseModel):
    pass


class MySQLBackup(Backup):
    mysql: str
    op: Union[Data, Log]


class TdsqlBackup(Backup):
    tdsql: str
    op: Union[TdSqlLog, ProxyLog]


class OBackup(Backup):
    osql: str
    op: Union[ProxyOLog, OData]


class Info(BaseModel):
    operate: Union[TdsqlBackup, MySQLBackup, OBackup]
    # @classmethod
    # def create_info(cls, operate: Union[MySQLBackup, TdsqlBackup]):
    #     return cls(operate=operate)


if __name__ == "__main__":
    info_dict = {
        "operate": {
            "tdsql": "db_type",
            "op": {"proxy_log": "backup_type"},
        }
    }

    info = Info(**info_dict)
    print("info", info)
    info.operate.op.print_a()
    # tdsql = TdsqlBackup(**{"tdsql": "db_type", "op": {"proxylog": "backup_type"}})
    # print("tdsql", tdsql)
