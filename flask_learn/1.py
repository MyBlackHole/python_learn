from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    return "ok"


if __name__ == "__main__":
    app.run(
        ssl_context=(
            r"/home/black/Documents/Code/Python/python_learn/flask_learn/secret.pem",
            r"/home/black/Documents/Code/Python/python_learn/flask_learn/secret.key",
        )
    )
