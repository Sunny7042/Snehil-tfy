from flask import Flask
import os
import sys

app = Flask(__name__)

# Use os.environ to get the secret from the YAML 'env' section
secret_value = os.environ.get("SNEHIL_SERV")

# We use flush=True to force the text into the TrueFoundry logs immediately
print("--- APP STARTUP ---", flush=True)

if secret_value:
    # NOTE: TrueFoundry may show this as ******** in the dashboard for safety
    print(f"[DEBUG] Secret SNEHIL_SERV found! Value: {secret_value}", flush=True)
else:
    print("[ERROR] Secret SNEHIL_SERV NOT found in environment!", flush=True)

@app.route("/")
def index():
    if secret_value:
        return "Secret is active! View logs in the TrueFoundry dashboard."
    return "Secret is missing from the environment."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
