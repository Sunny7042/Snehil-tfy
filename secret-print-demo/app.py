from flask import Flask
import os

app = Flask(__name__)

SECRET_PATH = "/var/secrets/snehil-serv/password"

secret_value = "SECRET_NOT_FOUND"

if os.path.exists(SECRET_PATH):
    with open(SECRET_PATH, "r") as f:
        secret_value = f.read().strip()

# PRINT SECRET IN LOGS
print(f"[SECRET] {secret_value}")

@app.route("/")
def index():
    return "Service started. Check logs for secret value."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




