from flask import Flask
import os
import sys

app = Flask(__name__)

# Fetching the secret from Environment Variables (set in YAML)
# TrueFoundry UI might mask this as ******** in logs
secret_value = os.environ.get("SNEHIL_SERV")

# This will print to the console as soon as the app starts
print("--- STARTING SECRET CHECK ---", flush=True)

if secret_value:
    print(f"[SUCCESS] Found SNEHIL_SERV. Value: {secret_value}", flush=True)
else:
    print("[ERROR] SNEHIL_SERV not found in environment!", flush=True)

@app.route("/")
def index():
    if secret_value:
        return "Secret loaded successfully! Check your TrueFoundry logs."
    return "Secret missing from environment."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
