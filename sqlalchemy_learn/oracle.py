# import oracledb
from urllib.parse import quote_plus as urlquote
from sqlalchemy.exc import NoResultFound

from sqlmodel import Field, Session, SQLModel, create_engine

DEFAULT_ORACLE_CHARSET = "utf-8"
DB_READ_TIMEOUT = 5
DB_WRITE_TIMEOUT = 5
DB_ECHO = False

class DBConnectInfo(SQLModel):
    hostname: str
    port: int
    username: str
    password: str
    database: str
    read_timeout: int = Field(default=DB_READ_TIMEOUT)
    write_timeout: int = Field(default=DB_WRITE_TIMEOUT)

    def get_url(self) -> str:
        raise

class DBClient(SQLModel):
    mysql_connect_info: DBConnectInfo

    def _get_engine(self):
        if not self.mysql_connect_info:
            raise

        return create_engine(
            self.mysql_connect_info.get_url(),
            echo=DB_ECHO,
        )

    def session_exec_one(self, sql):
        try:
            with Session(self._get_engine()) as session:
                ret = session.exec(sql)
                return ret.one()
        except NoResultFound as e:
            raise e

    def session_exec_all(self, sql):
        with Session(self._get_engine()) as session:
            ret = session.exec(sql)
            return ret.all()


class OracleConnectInfo(DBConnectInfo):
    charset: str = Field(default=DEFAULT_ORACLE_CHARSET)

    def get_url(self) -> str:
        return f"oracle+oracledb://{urlquote(self.username)}:{urlquote(self.password)}@{self.hostname}:{self.port}/{self.database}?encoding={self.charset}&nencoding={self.charset}"


class OracleClient(DBClient):
    pass
    def get_block_change_tracking_status(self):
        sql = "select status from v$block_change_tracking;"
        ret = self.session_exec_one(sql)
        if not ret:
            raise
        return ret[0]


if __name__ == "__main__":
    # LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH PYTHONPATH=$(pwd) python3 db/oracle_client.py
    mysql_client = OracleClient(
        mysql_connect_info=OracleConnectInfo(
            hostname="192.168.80.21",
            port=1521,
            username="system",
            password="oracle",
            database="pdb1",
        )
    )
    ret = mysql_client.get_block_change_tracking_status()
    print(ret)
