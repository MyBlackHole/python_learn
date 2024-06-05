from flask import Flask
import json

app = Flask(__name__)

data = {
    "state_color_mapping": {
        "queued": "gray",
        "running": "lime",
        "success": "green",
        "shutdown": "blue",
        "restarting": "violet",
        "failed": "red",
        "up_for_retry": "gold",
        "up_for_reschedule": "turquoise",
        "upstream_failed": "orange",
        "skipped": "pink",
        "removed": "lightgrey",
        "scheduled": "tan",
        "deferred": "mediumpurple",
        "sensing": "mediumpurple",
        "None": "lightblue",
    },
}


@app.route("/")
def get():
    return json.dumps(data)


if __name__ == "__main__":
    app.run(
        # ssl_context=(
        #     r"./secret.pem",
        #     r"./secret.key",
        # )
    )
