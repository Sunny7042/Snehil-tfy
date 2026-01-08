import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    secret_value = os.getenv("MY_SECRET", "SECRET_NOT_FOUND")
    return f"Secret value: {secret_value}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
