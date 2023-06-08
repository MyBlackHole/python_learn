# -*- coding: utf-8 -*-
import json
import logging
import os
from pathlib import Path

import psutil
from entity.project import Project, Process, dumps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    datefmt="%a, %d %b %Y %H:%M:%S",
    filename="./monitor.log",
    filemode="a",
)


def run_project(cmd):
    return psutil.Popen(
        ["python.exe", str(cmd)], cwd=str(cmd.parent), creationflags=16
    ).pid


def write_conf(path, project_conf):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(project_conf))


def start_and_up_conf(project):
    cmd = project.process.cmd
    project.process.pid = run_project(cmd=cmd)
    logging.info(f" 重新启动 project：{project} ")
    path = project.project_path
    project_bat = dumps(project)
    project_bat.pop("project_path")
    write_conf(path=path, project_conf=project_bat)


class Monitor:
    def __init__(self, project_conf_path="project_conf.json"):
        self.project_conf_path = project_conf_path
        self.process_list = []
        self.project_conf = []
        self.init()

    def init(self):
        """
        初始化
        """
        self.init_process()
        self.init_project_conf()

    def init_process(self):
        """
        1、读取所有进程
        2、筛选所有包含 python and .py 的命令行
        3、添加到元组中
        """
        for i in psutil.process_iter():
            try:
                cmdline = i.cmdline()
                if len(cmdline) >= 2 and "python" in cmdline[0] and ".py" in cmdline[1]:
                    process = Process().loads({"pid": i.pid, "cmd": cmdline[1]})
                    self.process_list.append(process)
                    logging.info(f" process：{process.dumps()} ")
            except Exception as e:
                print(f" error：{e}")

    def init_project_conf(self):
        """
        初始化 project 配置
        """
        for item in self.read_conf():
            try:
                conf = self.read_conf(Path(item))
                conf["project_path"] = item
                self.project_conf.append(Project().loads(conf))
            except Exception as e:
                logging.info(f" path：{item}项目配置读取失败 error：{e} ")

    def read_conf(self, file_path=None):
        """
        读取配置
        """
        if not file_path:
            file_path = self.project_conf_path
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                conf = json.loads(f.read())
                return conf
        except Exception as e:
            raise Exception(f" {file_path} 读取失败 ")

    def execute(self):
        logging.info("*" * 100)
        logging.info("*" * 100)
        logging.info(" 监控开始!!! ")
        for project in self.project_conf:
            try:
                # 不在运行中程序列表的直接添加到重启列表
                if project.process not in self.process_list:
                    start_and_up_conf(project)
                    continue

                # 筛选出在运行中程序列表的程序异常的添加到重启
                param_dict = project.__dict__.copy()
                param_dict.pop("project_path")
                for param in param_dict.values():
                    if param.is_reboot():
                        pid = project.process.pid
                        if pid != 0:
                            os.system(f"taskkill /F /PID {pid}")
                            logging.info(f" PID：{pid} 关闭成功 ")
                        start_and_up_conf(project)
                        break
            except Exception as e:
                logging.info(f" 启动失败 project：{project} error：{e}")

        logging.info(" 监控完成退出!!! ")
        logging.info("*" * 100)
        logging.info("*" * 100)
        return 0


if __name__ == "__main__":
    print(Monitor().process_list)
    # print(Monitor().project_conf)
    # print(Monitor('project_conf.json').project_conf)
    # Monitor('project_conf.json').execute()
    Monitor().execute()
    # p.daemon = True
    # p.start()
