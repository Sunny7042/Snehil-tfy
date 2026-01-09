from flask import Flask
import os

app = Flask(__name__)

SECRET_PATH = "/var/secrets/snehil-serv/password"

@app.route("/")
def index():
    return "Service running - check logs for secret"

if os.path.exists(SECRET_PATH):
    with open(SECRET_PATH, "r") as f:
        value = f.read().strip()
    print(f"[SECRET] {value}")
else:
    print(f"[SECRET] File not found: {SECRET_PATH}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


