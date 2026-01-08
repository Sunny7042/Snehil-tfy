from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("/run/secrets/snehil-serv/password", "r") as f:
            secret_value = f.read().strip()
        return f"Secret value: {secret_value}"
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    print("Flask app starting...")
    app.run(host="0.0.0.0", port=8080)

