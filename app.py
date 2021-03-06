# flask_web/app.py

"""Test."""

from flask import Flask  # type: ignore

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Test."""
    return "Hey, we have Flask in a Docker container!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
