from flask import Flask
import os
import sys

app = Flask(__name__)

# 1. Force Python to output immediately
# 2. Look for the environment variable, NOT the file path
secret_value = os.environ.get("SNEHIL_SERV")

# This goes to the logs as soon as the container starts
print("--- APP STARTUP DEBUG ---", file=sys.stderr)
if secret_value:
    print(f"[FOUND] SNEHIL_SERV is set. Value length: {len(secret_value)}", file=sys.stderr)
    print(f"[VALUE] {secret_value}", file=sys.stderr, flush=True)
else:
    print("[ERROR] SNEHIL_SERV is NOT found in environment", file=sys.stderr, flush=True)

@app.route("/")
def index():
    return f"Status: {'Secret Loaded' if secret_value else 'Secret Missing'}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
