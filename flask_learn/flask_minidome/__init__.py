import datetime
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# print(__name__)
app = Flask(__name__)

# 常规使用
# # base_dir = os.path.abspath(os.path.dirname(__file__))
# # database_uri = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://BlackHole:1358244533@localhost/db_flask"

# 测试
base_dir = os.path.abspath(os.path.dirname(__file__))
database_uri = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

# 文件格式
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, 'static/img/user')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.permanent_session_lifetime = datetime.timedelta(days=7)
app.secret_key = b'fjajeiojafkjdsfjksjf'
db = SQLAlchemy(app)
# print(app)
