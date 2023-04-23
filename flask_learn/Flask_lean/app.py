from flask import (Flask, abort, make_response, render_template, request,
                   url_for)
from user_api import *
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    # if not name:
    #     print(name)
    #     return "hello"
    # else:
    #     return render_template('hello.html', name=name)
    return render_template("hello.html", name=name)


@app.route("/")
def hello_world():
    return "Hello World!!!"


@app.route("/index")
def index():
    return redirect(url_for("login"))


@app.route("/user/<username>")
def show_user_profile(username):
    return "User {}".format(username)


@app.route("/int/<int:post_id>")
def show_int_profile(post_id):
    return "int {}".format(post_id)


@app.route("/path/<path:path>")
def show_path_profile(path):
    return "path {}".format(path)


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about/", methods=["GET", "POST"])
def about():
    return "The about page"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("about"))
    print(url_for("about", next="/"))
    print(url_for("show_user_profile", username="John Doe"))


@app.route("/sum/<int:a>/<int:b>")
def get_sum(a, b):
    return "{0} + {1} = {2}".format(a, b, a + b)


with app.test_request_context("/hello", method="POST"):
    assert request.path == "/hello"
    assert request.method == "POST"
    print("assert")


@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            print("ok!!")
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    else:
        print("GET")
    # username = request.cookies.get('username')
    # print(username)
    # if username:
    #     return render_template('login.html', error=username)
    # resp = make_response(render_template('login.html', error=error))
    # resp.set_cookie('username', '1358244533')
    # return resp
    abort(401)


@app.errorhandler(401)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@app.errorhandler(401)
def not_found(error):
    resp = make_response(render_template("page_not_found.html"), 404)
    print(resp)
    return resp


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("/var/www/uploads/" + secure_filename(f.filename))
        return "ok!!"
    else:
        return "......"


if __name__ == "__main__":
    app.run()
