from flask import Flask
import os

app = Flask(__name__)

path = "/var/secrets/snehil-serv/password"

if os.path.exists(path):
    with open(path, "r") as f:
        value = f.read().strip()
    print(f"[SECRET] {value}")
else:
    print("[SECRET] File not found:", path)

@app.route("/")
def index():
    return "Check logs for secret value."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)





