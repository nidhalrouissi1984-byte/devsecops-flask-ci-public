import sqlite3

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.after_request
def set_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'none'"
    return response


@app.route("/")
def home():
    return "Hello DevSecOps!"


@app.route("/search")
def search():
    query = request.args.get("q", "")
    if len(query) > 200:
        abort(400, description="Requete trop longue")
    return jsonify({"results": f"Search results for: {query}"})


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")

    # Validation de l'entree : uniquement un entier positif
    if not user_id.isdigit():
        abort(400, description="id doit etre un entier positif")

    conn = sqlite3.connect(":memory:")
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
        # Requete parametree : plus d'injection SQL possible
        cursor.execute("SELECT id, name FROM users WHERE id = ?", (int(user_id),))
        result = cursor.fetchall()
    finally:
        conn.close()

    return jsonify(result)


if __name__ == "__main__":  # pragma: no cover
    app.run(host="127.0.0.1", port=5000, debug=False)
