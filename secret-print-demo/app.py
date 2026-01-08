from flask import Flask
import os

app = Flask(__name__)

# Use os.environ.get to read the secret you defined in your YAML
secret_value = os.environ.get("SNEHIL_SERV")

if secret_value:
    # This will print to your TrueFoundry logs
    print(f"[SECRET] Found in environment: {secret_value}")
else:
    print("[SECRET] Variable SNEHIL_SERV not found in environment")

@app.route("/")
def index():
    if secret_value:
        return "Secret is loaded! Check the Service Logs in TrueFoundry."
    return "Secret missing! Check your YAML 'env' section."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
