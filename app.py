from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return jsonify({"results": f"Search results for: {query}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
