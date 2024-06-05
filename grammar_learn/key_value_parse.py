s = """PKNAME="" NAME="sda" SIZE="53687091200" ROTA="1" MOUNTPOINT="" FSTYPE=""
PKNAME="sda" NAME="sda1" SIZE="2097152" ROTA="1" MOUNTPOINT="" FSTYPE=""
PKNAME="sda" NAME="sda2" SIZE="209715200" ROTA="1" MOUNTPOINT="/boot" FSTYPE="xfs"
PKNAME="sda" NAME="sda3" SIZE="53474230272" ROTA="1" MOUNTPOINT="" FSTYPE="LVM2_member"
PKNAME="sda3" NAME="centos-root" SIZE="53473181696" ROTA="1" MOUNTPOINT="/" FSTYPE="xfs"
PKNAME="" NAME="sdb" SIZE="53687091200" ROTA="1" MOUNTPOINT="" FSTYPE=""
PKNAME="" NAME="sr0" SIZE="1073741312" ROTA="1" MOUNTPOINT="" FSTYPE="""""


def parse_kvs(raw: str):
    rows = raw.split("\n")
    dicts = []
    for row in rows:
        if not row:
            continue

        d = dict()
        row = row.strip()
        cols = row.split(" ")
        for col in cols:
            if not col:
                continue

            col.strip()
            kv = col.split("=")
            d[kv[0].strip().lower()] = kv[1].strip().strip('"')
        dicts.append(d)
    return dicts


print(parse_kvs(s))
