#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          fdfs_tool
   Description:
   Author:             Black Hole
   date:               2020/12/14
-------------------------------------------------
   Change Activity:    2020/12/14:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import os
from pathlib import Path

from fdfs_client.client import get_tracker_conf, Fdfs_client


class FDFSTool(object):
    fast_tool = None

    def __new__(cls, *args, **kwargs):
        if not cls.fast_tool:
            cls.fast_tool = object.__new__(cls, *args, **kwargs)
        return cls.fast_tool

    def __init__(self, conf_path: str = None):
        local_conf = Path(os.path.abspath(__file__)).parent / 'client.conf'
        if not conf_path:
            conf_path = str(local_conf)
        self._tracker_conf = get_tracker_conf(conf_path=conf_path)
        self.client = Fdfs_client(self._tracker_conf)

    def upload_file(self, file_path: str):
        """
        文件上传
        Return:{
            'Group name': b'group1',
            'Remote file_id': b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt',
            'Status': 'Upload successed.',
            'Local file name': 'test.txt',
            'Uploaded size': '12B',
            'Storage IP': b'192.168.31.220'
        }
        """
        return self.client.upload_by_filename(filename=file_path)

    def download_file(self, local_file: str, remote_file_id: bytes):
        """
        文件下载
        Return:{
            'Remote file_id': b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt',
            'Content': 't.txt',
            'Download size': '12B',
            'Storage IP': b'192.168.31.220'
        }
        """
        return self.client.download_to_file(local_filename=local_file, remote_file_id=remote_file_id)

    def delete_file(self, remote_file_id: bytes):
        """
        文件删除
        Return: ('Delete file successed.', b'group1/M00/00/00/wKgf3F5MAe2AV_23AAAADL_GVeU370.txt', b'192.168.31.220')
        """
        return self.client.delete_file(remote_file_id=remote_file_id)


if __name__ == "__main__":
    fdfs_tool = FDFSTool()
    print(fdfs_tool.upload_file(r"./client.conf"))
