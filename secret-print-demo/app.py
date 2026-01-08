import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("/var/secrets/snehil-serv/password", "r") as f:
            secret_value = f.read().strip()
    except:
        secret_value = "SECRET_NOT_FOUND"

    return f"Secret value: {secret_value}"

app.run(host="0.0.0.0", port=8080)
