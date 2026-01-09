import os
import time
from fastapi import FastAPI

app = FastAPI()

SECRET_PATH = "/var/secrets/snehil-serv/password"
MODE = os.getenv("MODE", "print-secret")

secret_value = "SECRET_NOT_FOUND"

if os.path.exists(SECRET_PATH):
    with open(SECRET_PATH, "r") as f:
        secret_value = f.read().strip()

if MODE == "print-secret":
    print("Secret value:", secret_value)
    time.sleep(3600)

else:
    print(f"Unknown MODE: {MODE}")
    time.sleep(3600)
