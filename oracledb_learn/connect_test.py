import oracledb

# oracledb.init_oracle_client()

# os.environ["PYO_SAMPLES_ADMIN_PASSWORD"] = pw

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
        sql = "select log_mode from v$database"
        cursor.execute(sql)
        for row in cursor:
            print("Row:", row)
