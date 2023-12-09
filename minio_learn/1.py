import minio

minio_conf = {
    "endpoint": "127.0.0.1:9000",
    "access_key": "12345678",
    "secret_key": "12345678",
    "secure": False,
}
# pip install minio


def up_data_minio(bucket: str, object_name: str, file_path: str):
    client = minio.Minio(**minio_conf)
    client.fput_object(
        bucket_name=bucket,
        object_name=file_path,
        file_path=file_path,
        content_type="application/zip",
    )


def load_data_minio(bucket: str):
    client = minio.Minio(**minio_conf)
    if not client.bucket_exists(bucket):
        return None
    data = client.get_object(bucket, "1.py")
    with open("1.py", "wb") as file_data:
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return data.data


file_path = "util_minio.py"

up_data_minio("wdg1", file_path, file_path)
# load_data_minio('test')
