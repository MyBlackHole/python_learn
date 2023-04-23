#!/bin/python3

import pymysql

localhost_db = {
    "host": "192.168.90.204",
    "user": "teledb",
    "passwd": "teledb",
    "db": "teledb",
    "port": 9095,
}
prod_inst_id = 1
res_id = 1

sql = (
    "select a.host, a.port, b.sys_user, b.sys_password, b.ssh_port, c.db_ag_user, c.db_ag_password, \
    concat(a.db_path,'/etc/', d.parameter_group_used,'.cnf') mysqlcnf from db_resource a left join machine_resource b \
    on a.machine_id = b.id left join db_user_info c on a.res_id = c.res_id left join paas_product d \
    on a.prod_inst_id = d.prod_inst_id left join monitor_cluster_db_states e on a.prod_inst_id = e.prod_inst_id "
    # on a.prod_inst_id = d.prod_inst_id left join monitor_cluster_db_states e on a.prod_inst_id = e.prod_inst_id \
    # where a.prod_inst_id = "
    # + str(prod_inst_id)
    # + " and a.res_id = "
    # + str(res_id)
    # + " and a.alive = 0 and e.repl = 0 limit 1"
)

# # (('192.168.90.204', '5555', '/teledb/teleapps/mysql5555/etc/'), ('192.168.90.205', '5555', '/teledb/teleapps/mysql5555/etc/'), ('192.168.90.206', '5555', '/teledb/teleapps/mysql5555/etc/'), ('192.168.90.205', '6666', '/teledb/teleapps/mysql6666/etc/'), ('192.168.90.204', '6666', '/teledb/teleapps/mysql6666/etc/'), ('192.168.90.206', '6666', '/teledb/teleapps/mysql6666/etc/'), ('192.168.90.206', '7777', '/teledb/teleapps/mysql7777/etc/'), ('192.168.90.205', '7777', '/teledb/teleapps/mysql7777/etc/'), ('192.168.90.204', '7777', '/teledb/teleapps/mysql7777/etc/'))
# sql = "select a.host, a.port, concat(a.db_path,'/etc/') mysqlcnf from db_resource a"

# # (('mysql5555.cnf', 1), ('mysql6666.cnf', 2), ('mysql7777.cnf', 3))
# sql = "select concat(d.parameter_group_used,'.cnf') mysqlcnf, d.prod_inst_id from paas_product d"


# # (('teledb', 'Ti84oTg1', '22'), ('teledb', 'Ti84oTg1', '22'), ('teledb', 'Ti84oTg1', '22'), ('teledb', 'Ti84oTg1', '22'))
# sql = "select b.sys_user, b.sys_password, b.ssh_port from machine_resource b"

# # (('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'), ('RDS_agent', 'yl1t4PnHFbVPbz0wKFBB'))
# sql = "select c.db_ag_user, c.db_ag_password from db_user_info c"

db = pymysql.Connect(
    host=localhost_db["host"],
    port=localhost_db["port"],
    user=localhost_db["user"],
    passwd=localhost_db["passwd"],
    db=localhost_db["db"],
)


cursor = db.cursor()
cursor.execute(sql)
print(cursor._executed)
print(cursor.fetchall())
cursor.close()
db.close()
