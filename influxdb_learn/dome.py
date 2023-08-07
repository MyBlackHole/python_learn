import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# from pillow_learn.pillow-lean02.01 import buildvector

token = os.environ.get(
    "INFLUXDB_TOKEN",
    "3cZY5pYkkU3t3xXOwhXGNn6DvDs3wica8WQI5mTaHO6ME_rhuFSo7c773pkw_5n1slPSGANOYvyEJsz-U_RNbg==",
)
org = "test"
bucket = "test"
url = "http://127.0.0.1:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api = write_client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    point = (
        Point("measurement1")
        .tag(
            "tagname1",
            "tagvalue1",
        )
        .field(
            "field1",
            value,
        )
    )
    write_api.write(
        bucket=bucket,
        org=org,
        record=point,
    )
    time.sleep(1)  # separate points by 1 second


query_api = write_client.query_api()

query = """from(bucket: "test")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="test")

for table in tables:
    for record in table.records:
        print(record)
