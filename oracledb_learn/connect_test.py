import json
import oracledb
import datetime

# oracledb.init_oracle_client()

# os.environ["PYO_SAMPLES_ADMIN_PASSWORD"] = pw


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


c = None


if __name__ == "__main__":
    # LD_LIBRARY_PATH=/media/black/Data/lib/oracle/instantclient_21_12:$LD_LIBRARY_PATH PYTHONPATH=$(pwd) python3 connect_test.py
    c = oracledb.connect(
        user="system",
        password="oracle",
        dsn="192.168.80.21/pdb1",
        tcp_connect_timeout=5,
    )
    print(c.ping())
    with c.cursor() as cursor:

        # sql = "select * from v$database"

        # sql = "select * from v$parameter"

        # sql = "select * from dba_data_files"

        # sql = "select * from v$version"

        # sql = "select * from gv$datafile"

        # sql = "select * from gv$instance"

        # sql = "select * from v$pdbs"

        # sql = "SELECT * FROM PRODUCT_COMPONENT_VERSION"

        # sql = "select * from dba_temp_files"

        # sql = "select * from v$log "

        # sql = "select * from dual"

        # sql = "select SYS_CONTEXT ('USERENV','ORACLE_HOME') as oracle_home from dual"

        # sql = "select * from gv$archived_log"

        # sql = "select * from v$session_longops"

        # sql = "alter session set container=CDB$ROOT"
        # cursor.execute(sql)

        # sql = "select * from v$block_change_tracking"

        # sql = "select * from v$datafile"

        # sql = "select * from v$controlfile"

        # sql = "select * from v$logfile"

        # sql = "select * from V$ASM_DISKGROUP"

        # sql = "select * from v$instance"

        sql = "select * from v$tempfile"

        cursor.execute(sql)
        print("HEAD: ", cursor.description)
        columns = [col.name for col in cursor.description]
        cursor.rowfactory = lambda *args: dict(zip(columns, args))
        for row in cursor:
            print("Row:", row)
            # row["SQL_ADDRESS"] = ""
            print(json.dumps(row, cls=DateEncoder))
