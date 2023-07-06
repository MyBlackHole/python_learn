#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import threading
import time
from os import getpid, path
from threading import Thread
from flask import Flask
from flask import jsonify


def thread_test():
    while True:
        lock = threading.Condition()
        lock.acquire()
        print(getpid())
        # dosomething(have some socket communication)
        print("input thread")
        lock.release()


t = Thread(target=thread_test)
s = Thread(target=thread_test)
s.setDaemon(True)
t.setDaemon(True)
t.start()
s.start()


application = Flask(__name__)


@application.route("/v1/demo", methods=["GET"])
def test_invoke_chain():
    data = {"code": 0, "msg": "success", "data": {}}
    time.sleep(1000)
    return jsonify(data)


@application.route("/v2/demo", methods=["GET"])
def test_invoke_chain_demo2():
    data = {"code": 0, "msg": "success", "data": {}}
    return jsonify(data)

# uwsgi --http-socket :9090 --enable-threads --plugin python3 --wsgi-file app.py
# uwsgi --http :9090 --enable-threads --gevent 100  --wsgi-file app.py
# gevent 开启协程
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=900, debug=True, threaded=True)
