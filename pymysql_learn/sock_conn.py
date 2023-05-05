import pymysql

unix_socket = "/var/run/mysqld/mysqld.sock"

table_key = "Tables_in_test_xa"

localhost_db = {
    "host": "192.168.90.204",
    "user": "teledb",
    "passwd": "teledb",
    "db": "iam",
    "port": 9095,
}

db = pymysql.Connect(
    # host=localhost_db["host"],
    # port=localhost_db["port"],
    cursorclass=pymysql.cursors.DictCursor,
    user=localhost_db["user"],
    passwd=localhost_db["passwd"],
    db=localhost_db["db"],
    unix_socket=unix_socket,
)

db.ping()

cursor = db.cursor()
cursor.execute("show tables;")
data = cursor.fetchall()
print(data)

select_table_all_sql = "select * from `%s`"
for value in data:
    sql = select_table_all_sql % value[table_key]
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    print("*" * 300)
