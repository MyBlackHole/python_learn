from kazoo.client import KazooClient

zk = KazooClient()
transaction = zk.transaction()
transaction.check("/china/hebei", version=3)
transaction.create("/china/shanxi", b"thi is shanxi.")
results = transaction.commit()
