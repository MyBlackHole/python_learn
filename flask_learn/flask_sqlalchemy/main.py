import time

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.session import _app_ctx_id

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://black:1358@localhost/flask_sqlalchemy_test"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)


@app.route("/sleep")
def sleep():
    print(id(db))
    print(id(db.session))
    print(id(db.session))
    print(_app_ctx_id())
    db.session.add(User(username=request.args.get("username")))
    time.sleep(20)
    db.session.commit()
    return "ok"


@app.route("/get")
def get():
    print(id(db))
    print(id(db.session))
    print(id(db.session))
    print(_app_ctx_id())
    print(_app_ctx_id())
    print(_app_ctx_id())
    db.session.add(User(username=request.args.get("username")))
    db.session.commit()
    return "ok"


app.run()
