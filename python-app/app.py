from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)
redis_client = Redis()
@app.route("/login", methods=["POST"])
def login():
    name = request.form["username"]
    redis_client.incr(name)
    return {"name": name, "msg": "login success", "count": redis_client.get(name)}


if __name__ == "__main__":
    app.run(port=5000)

