import pymysql
from retrying import retry

from loguru_learn.log import logger


class Results(object):
    def __init__(self):
        self.success = False
        self.data = []
        self.error = ""


def iteration_is_none(item):
    try:
        if item is None or len(item) <= 0:
            return True
        else:
            return False
    except Exception as e:
        logger.exception(e)
        return True


DEFAULT_DATABASE = {
    "host": "127.0.0.1",
    "user": "black",
    "password": "1358",
    "database": "test",
    "port": 3306,
}


def mysql_decorator(func):
    def connection(*args, **kwargs):
        database_info = kwargs.get("database_info", DEFAULT_DATABASE)
        database_info = (
            DEFAULT_DATABASE if iteration_is_none(database_info) else database_info
        )
        assert all(
            key in database_info.keys()
            for key in ["host", "user", "password", "database", "port"]
        ), "数据库信息缺少必要key  'host','user','password','database','port'"
        conn = pymysql.connect(
            **database_info,
            cursorclass=pymysql.cursors.DictCursor,
            read_timeout=30,
            write_timeout=30
        )
        cursor = conn.cursor()

        def wrapper(*args, **kwargs):
            kwargs["conn"] = conn
            kwargs["cursor"] = cursor
            return func(*args, **kwargs)

        results = wrapper(*args, **kwargs)
        cursor.close()
        conn.close()
        return results

    return connection


class MySQLManage(object):
    mysql_utility = None

    def __new__(cls, *args, **kwargs):
        if cls.mysql_utility is None:
            cls.mysql_utility = object.__new__(cls, *args, **kwargs)
        return cls.mysql_utility

    @mysql_decorator
    @retry(stop_max_attempt_number=3, stop_max_delay=1000)
    def select(self, sql, conn=None, cursor=None, database_info=None):
        results = Results()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            results.success = True
            results.data = data
        except Exception as e:
            print(e)
        return results

    def execute(self, sql, conn=None, cursor=None, database_info=None):
        return self._execute_db(
            "execute", sql, conn=conn, cursor=cursor, database_info=database_info
        )

    def executemany(self, sql, data, conn=None, cursor=None, database_info=None):
        return self._execute_db(
            "executemany",
            sql,
            data,
            conn=conn,
            cursor=cursor,
            database_info=database_info,
        )

    @mysql_decorator
    @retry(stop_max_attempt_number=3, stop_max_delay=1000)
    def _execute_db(self, func, *args, conn=None, cursor=None, database_info=None):
        results = Results()
        try:
            # 通过 (str) func 执行不同方法
            rows = getattr(cursor, func)(*args)
            conn.commit()
            results.success = True
            results.data = rows
        except Exception as e:
            print(e)
        return results
