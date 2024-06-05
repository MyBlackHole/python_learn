import io
import csv

# ret_list = []
# with open('tmp.csv') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', skipinitialspace=True)
#     spamreader = [item for item in spamreader]
#     h = spamreader[0]
#     for row in spamreader[1:]:
#         ret = {}
#         for i, row in enumerate(row):
#             ret[h[i]] = row
#         ret_list.append(ret)


# print(ret_list)


csv_str = """NAME                                                                   CREATION       VOLSIZE
        aiopool/aio_4089108a1417_20_43_1690442448_goldendb_data@1690768835917  1690768964  3221225472
"""

# csv_str = """PKNAME NAME SIZE ROTA MOUNTPOINT FSTYPE
# sda 53687091200 1
# sda sda1 2097152 1
# sda sda2 209715200 1 /boot xfs
# sda sda3 53474230272 1  LVM2_member
# sda3 centos-root 53473181696 1 / xfs
# sdb 53687091200 1
# sr0 1073741312 1
# """

csv_str_stream = io.StringIO(csv_str)

ret_list = []
spamreader = csv.reader(csv_str_stream, delimiter=' ', skipinitialspace=True)
spamreader = [item for item in spamreader]
h = spamreader[0]
for row in spamreader[1:]:
    ret = {}
    for i, row in enumerate(row):
        ret[h[i]] = row
    ret_list.append(ret)


print(ret_list)
