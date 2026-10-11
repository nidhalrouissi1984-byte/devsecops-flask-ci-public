from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello DevSecOps!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":  # pragma: no cover
    app.run(host="127.0.0.1", port=5000)
