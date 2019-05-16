from flask import Flask, request, jsonify, Response
from redis import Redis
import os

app = Flask(__name__)
redis_client = Redis(host=os.getenv('REDIS_HOST'))
@app.route("/login", methods=["POST"])
def login():
    name = request.form["username"]
    redis_client.incr(name)
    resp = jsonify({"name": name, "msg": "login success", "count": redis_client.get(name).decode()})
    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp


if __name__ == "__main__":
    app.run(port=5000)

