import json
import os
import sys
import traceback
from datetime import datetime, timedelta

import boto3
import requests
from botocore.exceptions import ClientError
from loguru import logger

# 可参考的官方文档记录
# https://docs.aws.amazon.com/cli/latest/reference/s3api/restore-object.html
# https://blog.csdn.net/defaultbyzt/article/details/103821684
# https://blog.csdn.net/defaultbyzt/article/details/103822358?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control

# 如何使用 AWS CLI 从 Amazon S3 Glacier 存储类还原 S3 对象？
# https://aws.amazon.com/cn/premiumsupport/knowledge-center/restore-s3-object-glacier-storage-class/

# 如何使用 Amazon S3 控制台中的还原层来还原 Amazon S3 Glacier 存储类中的已存档对象？
# https://aws.amazon.com/cn/premiumsupport/knowledge-center/restore-glacier-tiers/

this_file_path = sys.argv[0]  # 获取命令行第0个参数，即运行的文件名称

this_log_file_path = os.path.join(
    "./logs", this_file_path.split("/")[-1].split(".")[0] + ".log"
)
logger.info(f"this_log_file_path = {this_log_file_path}")

logger.add(this_log_file_path)

ACK = "xxxxxx"
ACS = "xxxxxxxxxxxx"

# s3
bucket_name = "your_bucket_name"  # s3桶名称
tmall_s3_remote_dir = "your_file_path_name"  # 要下载的s3文件夹

s3 = boto3.client(
    "s3",
    region_name="cn-north-4",
    aws_access_key_id=ACK,
    aws_secret_access_key=ACS,
)

# 文件路径
local_save_path = "./"  # s3文件下载到本地临时存储路径


class DingTalk(object):
    def __init__(
        self, webhook_url, author, title, at_mobile_list=None, is_at_all=False
    ):
        """
        :param webhook_url: 指定的url
        :param author: 任务所属，用于定位问题 例如 Task，Console
        :param title: 具体执行的文件
        :param at_mobile_list: 需要 @的人的手机号，传入list
        """
        self.url = webhook_url
        self.author = author
        self.title = title
        self.at_mobile_list = self.init_at_mobile_list(at_mobile_list)
        self.is_at_all = is_at_all

    @staticmethod
    def init_at_mobile_list(at_mobile_list):
        if at_mobile_list and isinstance(at_mobile_list, list):
            return at_mobile_list
        else:
            return []

    def send(self, msg):
        msg = {
            "msgtype": "text",
            "text": {"content": "{}{}{}".format(self.author, self.title, msg)},
            "at": {"atMobiles": self.at_mobile_list, "isAtAll": self.is_at_all},
        }

        headers = {"Content-Type": "application/json"}
        resp = requests.post(self.url, data=json.dumps(msg), headers=headers)


def _get_all_s3_objects(**base_kwargs):
    """
    获取s3_objects列表
    """
    try:
        continuation_token = None
        while True:
            list_kwargs = dict(MaxKeys=1000, **base_kwargs)
            if continuation_token:
                list_kwargs["ContinuationToken"] = continuation_token
            response = s3.list_objects_v2(**list_kwargs)
            yield from response.get("Contents", [])
            if not response.get("IsTruncated"):  # At the end of the list?
                break
            continuation_token = response.get("NextContinuationToken")
    except:
        # send_dingtalk_message(traceback.format_exc())
        logger.error(traceback.format_exc())


def create_assist_date(date_start=None, date_end=None):
    """
    生成指定时间段内的 Date Str List
    :param date_start: 开始时间
    :param date_end: 结束时间
    :return: date_list
    """
    if date_start is None:
        date_start = "2020-01-01"
    if date_end is None:
        date_end = datetime.now().strftime("%Y-%m-%d")

    # 转为日期格式
    date_start = datetime.strptime(date_start, "%Y-%m-%d")
    date_end = datetime.strptime(date_end, "%Y-%m-%d")
    date_list = [date_start.strftime("%Y-%m-%d")]
    while date_start < date_end:
        date_start += timedelta(days=+1)  # 日期叠加一天
        date_list.append(date_start.strftime("%Y-%m-%d"))  # 日期转字符串存入列表

    return date_list


class ZipS3TmallFiles(object):
    def __init__(self):
        self.s3_file_path = ""  # 要下在的s3路径
        self.local_file_path = ""  # s3下载后本地存储路径
        self.local_zip_file_path = ""  # 本地压缩文件存储路径
        self.error_item_count = 0
        self.execute_delete = True

    # days还原出来的临时对象有效天数，到期后自动删除，不包括还原出来当天。
    def restore_object(self, bucket_name, object_name, days, retrieval_type="Standard"):
        request = {"Days": days, "GlacierJobParameters": {"Tier": retrieval_type}}
        # s3 = boto3.client('s3')
        try:
            s3.restore_object(
                Bucket=bucket_name, Key=object_name, RestoreRequest=request
            )
        except ClientError as e:
            logger.error(e)
            logger.error(
                f"NoSuchBucket, NoSuchKey, or InvalidObjectState error == the object's, storage class was not GLACIER. {bucket_name} {object_name} "
            )

            return False
        return True

    # 查看对象 bucket_name桶名 object_name对象名
    def head_object(self, bucket_name, object_name):
        s3 = boto3.client("s3")
        response = None
        try:
            response = s3.head_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            logger.error(e)
            logger.error(
                f"NoSuchBucket, NoSuchKey, or InvalidObjectState error == the object's, storage class was not GLACIER. {bucket_name} {object_name} "
            )
            return None
        return response

    def download_s3_files(
        self,
    ):
        # 获取s3_objects列表
        s3_objects = _get_all_s3_objects(Bucket=bucket_name, Prefix=tmall_s3_remote_dir)
        key_content_list = []
        total_content_size = 0

        # task_pool = threadpool.ThreadPool(tp_size)
        for contents in s3_objects:
            key_value = contents.get("Key", None)
            file_size = contents.get("Size", 0)
            if "size_384.zip" in key_value:
                # logger.info(f"key_value = {key_value}")

                key_content_list.append(key_value)
                total_content_size += file_size

        total_item_count = len(key_content_list)
        # if total_item_count > 0:
        #     key_content_list.pop(0)

        temp_info = (
            "list Objects, Objects Count: {}, "
            "Total Size Is: {} GB | pid = {} | ppid = {}".format(
                total_item_count,
                total_content_size / 1024 / 1024 / 1024,
                os.getpid(),
                os.getppid(),
            )
        )
        logger.info(temp_info)

        # logger.info(f"key_content_list = {key_content_list}")
        done_count, doing_count, need_count = 0, 0, 0
        for index, key_name in enumerate(key_content_list):
            logger.info(f"---------------------------------------")
            logger.info(f"key_name before = {key_name}")
            # 检查还原状态
            success = self.head_object(bucket_name, key_name)
            # logger.info(f"success = {success}")
            if success:
                if success.get("Restore"):
                    logger.info("Restore {}".format(success["Restore"]))
                    index = success["Restore"].find('ongoing-request="false"')
                    if -1 == index:
                        logger.info(f"{index} 正在还原...{key_name}")
                        doing_count += 1
                    else:
                        logger.info(
                            success["Restore"][
                                success["Restore"].find("expiry-date=") :
                            ]
                        )
                        logger.info(f"{index} 还原成功...{key_name}")
                        done_count += 1
                else:
                    logger.info(f"{index} 需要还原... {key_name}")
                    self.restore_object(bucket_name, key_name, 10)
                    need_count += 1
        logger.info(
            f"total_count: {total_item_count}, done_count: {done_count}, doing_count: {doing_count}, need_count: {need_count}"
        )


if __name__ == "__main__":
    """启动还原脚本"""
    # 初始化实例
    zip_s3_files = ZipS3TmallFiles()

    # 从s3下载文件
    zip_s3_files.download_s3_files()
