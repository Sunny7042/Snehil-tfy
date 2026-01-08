from flask import Flask
import os

app = Flask(__name__)

# READ SECRET FROM MOUNTED FILE
secret_file = "/var/secrets/snehil-serv/password"
secret_value = "SECRET_NOT_FOUND"

if os.path.exists(secret_file):
    with open(secret_file, "r") as f:
        secret_value = f.read().strip()

# PRINT SECRET TO LOGS
print(f"[SECRET] {secret_value}")

@app.route("/")
def index():
    return f"Hello! Secret logged successfully."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



