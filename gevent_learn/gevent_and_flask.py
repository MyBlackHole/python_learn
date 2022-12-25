#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   gevent_and_flask
   Description:
   Author:      Black Hole
   date:        2020/6/1
-------------------------------------------------
   Change Activity:
                2020/6/1:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# coding: utf-8
# code by https://cpp.la, 2020-04-20
# flask + gevent + multiprocess + wsgi

from gevent import monkey

monkey.patch_all()

from gevent.pywsgi import WSGIServer
import datetime
import os
from multiprocessing import cpu_count, Process
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/cppla", methods=['GET'])
def function_benchmark():
    return jsonify(
        {
            "status": "ok",
            "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
            "pid": os.getpid()
        }
    ), 200


def server_forever(server):
    server.start_accepting()
    server._stop_event.wait()


def run(multi_process):
    if not multi_process:
        WSGIServer(('0.0.0.0', 8080), app).serve_forever()
    else:
        mulserver = WSGIServer(('0.0.0.0', 8080), app)
        mulserver.start()

        for i in range(cpu_count()):
            p = Process(target=server_forever, args=(mulserver,))
            p.start()


if __name__ == "__main__":
    # 单进程 + 协程
    run(False)
    # 多进程 + 协程
    # run(True)
