import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "oneapp")
PORT = int(os.getenv("PORT", "5050"))


@app.route("/")
def home():
    return jsonify(
        application=APP_NAME,
        message="Hello from the Jenkins CI/CD lab"
    )


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        application=APP_NAME
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )