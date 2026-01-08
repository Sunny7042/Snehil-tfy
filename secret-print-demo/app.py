from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    possible_paths = [
        "/run/secrets",
        "/var/run/secrets",
        "/var/secrets",
        "/secrets"
    ]

    output = []
    for base in possible_paths:
        if os.path.exists(base):
            try:
                entries = os.listdir(base)
                output.append(f"{base}: {entries}")
            except Exception as e:
                output.append(f"{base}: ERROR ({e})")
        else:
            output.append(f"{base}: NOT FOUND")

    # Try direct secret access guesses
    guesses = [
        "/run/secrets/snehil-serv/password",
        "/var/run/secrets/snehil-serv/password",
        "/var/secrets/snehil-serv/password",
        "/secrets/snehil-serv/password"
    ]

    for g in guesses:
        if os.path.exists(g):
            try:
                with open(g, "r") as f:
                    output.append(f"FOUND at {g}: {f.read().strip()}")
            except Exception as e:
                output.append(f"ERROR reading {g}: {e}")
        else:
            output.append(f"NOT FOUND: {g}")

    return "<br>".join(output)

if __name__ == "__main__":
    print("Service started")
    app.run(host="0.0.0.0", port=8080)


