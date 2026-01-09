import os
import time
from fastapi import FastAPI

app = FastAPI()

# Mounted secret file path based on your YAML + UI
SECRET_PATH = "/var/secrets/snehil-serv/password"

# Read secret from mounted file
if os.path.exists(SECRET_PATH):
    with open(SECRET_PATH, "r") as f:
        MY_SECRET = f.read().strip()
else:
    MY_SECRET = "SECRET_NOT_FOUND"

# MODE logic same as colleague
MODE = os.getenv("MODE", "print-secret")

# Service 1 — Print Secret
if MODE == "print-secret":
    print("Secret value:", MY_SECRET)
    time.sleep(3600)

# Service 4 — HTTP Endpoint (optional)
elif MODE == "helloworld":
    print("Secret value on startup:", MY_SECRET)

    @app.get("/")
    def hello():
        return {"message": "Hello World"}

    @app.get("/secret")
    def get_secret():
        return {"secret": MY_SECRET}

else:
    print(f"Unknown MODE: {MODE}")
    time.sleep(3600)

