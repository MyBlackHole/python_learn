#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   project
   Description:
   Author:      Black Hole
   date:        2020/7/1
-------------------------------------------------
   Change Activity:
                2020/7/1:
-------------------------------------------------
"""

__author__ = "Black Hole"

from pathlib import Path

import cattr
from attr import attrs, attrib, asdict, astuple
from loguru import logger
from utility.monitor import file_monitor, url_monitor

cattr.register_unstructure_hook(Path, lambda path: str(path))
cattr.register_structure_hook(Path, lambda string, _: Path(string))
dumps = cattr.unstructure
loads = cattr.structure


class Ob(object):
    def dumps(self):
        return dumps(self)

    def loads(self, d: dict):
        return loads(d, self.__class__)

    def as_dict(self):
        return asdict(self)

    def as_tuple(self):
        return astuple(self)


@attrs
class Process(Ob):
    # 进程pid
    pid = attrib(type=int, default=0)
    # 项目执行文件路径
    cmd = attrib(type=Path, default=Path())

    def is_reboot(self):
        if self.pid == 0:
            return True
        return False


@attrs
class FileMonitor(Ob):
    # 需要监控的文件路径
    file_path = attrib(type=Path, default=Path())
    # 等待时间
    wait_time = attrib(type=int, default=10)
    # 等待前后差值大小
    diff_size = attrib(type=int, default=0)

    def is_reboot(self):
        if self.file_path == Path():
            return False
        if self.is_result():
            return False
        return True

    def is_result(self):
        try:
            return file_monitor(
                file_path=self.file_path,
                wait_time=self.wait_time,
                diff_size=self.diff_size,
            )
        except Exception as e:
            logger.exception(f"{e}")
        return False


@attrs
class RequestMonitor(Ob):
    # 需要监控的url
    url = attrib(type=str, default="")

    def is_reboot(self):
        if self.is_result():
            return True
        return False

    def is_result(self):
        if self.url == "":
            return False
        if url_monitor(self.url):
            return False
        return True


@attrs
class Project(Ob):
    # 项目路径
    project_path = attrib(type=Path, default=Path())
    # 进程配置
    process = attrib(type=Process, default=Process())
    # 文件监控配置
    file_monitor = attrib(type=FileMonitor, default=FileMonitor())
    # url监控
    url_monitor = attrib(type=RequestMonitor, default=RequestMonitor())


if __name__ == "__main__":
    # file_monitor = FileMonitor()
    # print(file_monitor.dumps())
    project = Project()
    print(project.dumps())
    param_dict = project.__dict__.copy()
    param_dict.pop("name")
    print(param_dict.values())
    print(project.dumps())
    # print(process)
    # print(Process().dumps({'pid': 1, 'cmd': '.'}))
    # print(Process().loads())
    # print(Project().dumps())
    # print(Project().loads({'name': '', 'process': {'pid': 0, 'cmd': '.'}}))
    # with open('../project.json', 'r', encoding='utf-8') as f:
    #     for item in json.loads(f.read()):
    #         print(Project().loads(item))
    # print(f'{Process()}')
