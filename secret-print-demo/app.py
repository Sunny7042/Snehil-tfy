from flask import Flask
import os

app = Flask(__name__)

# Use flush=True to bypass buffering
secret_value = os.environ.get("SNEHIL_SERV")

print("--- STARTING APP ---", flush=True)

if secret_value:
    print(f"[SECRET] Value found: {secret_value}", flush=True)
else:
    print("[SECRET] Not found in environment!", flush=True)

@app.route("/")
def index():
    return "Check logs for secret value."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
