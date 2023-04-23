import rocksdb
import asyncio
from rocksdb.rocksdb_ext import Response


async def main():
    db = rocksdb.RocksDB(
        db_path="myrocksdb/", options=rocksdb.Options(create_if_missing=True)
    )

    key = "123-456-789"
    response = await db.put(rocksdb.WriteOptions(), key, "Hello world. Bye!")

    if response.status.ok:  # You always need to check if the request success.
        get_value = await db.get(rocksdb.ReadOptions(), key)

        print(get_value.value)  # Hello world. Bye!

        await db.delete(rocksdb.WriteOptions(), key)
    else:
        print(get_value.status.to_dict())

    await db.close()


asyncio.run(main())
