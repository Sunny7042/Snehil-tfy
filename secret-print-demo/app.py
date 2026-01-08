from flask import Flask
import os

app = Flask(__name__)

# Fetching from the Environment Variable defined in your YAML
# The key 'SNEHIL_SERV' must match the key in your YAML 'env' section
secret_value = os.environ.get("SNEHIL_SERV")

if secret_value:
    print(f"[SECRET] Found in environment: {secret_value}")
else:
    print("[SECRET] Not found in environment variables.")

@app.route("/")
def index():
    if secret_value:
        return f"Secret found! Check your logs to see the value."
    return "Secret not found in environment."

if __name__ == "__main__":
    # Ensure port matches the port in your YAML (8080)
    app.run(host="0.0.0.0", port=8080)
