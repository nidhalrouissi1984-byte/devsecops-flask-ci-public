
from flask import Flask, request, jsonify
import sqlite3

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps!"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return jsonify({"results": f"Search results for: {query}"})

@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")

    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
