import os
from fastapi import FastAPI

app = FastAPI()

# --- SECRET ---
MY_SECRET = os.getenv("MY_SECRET", "SECRET_NOT_FOUND")

# --- VOLUME ---
VOLUME_PATH = "/mnt/data"
TEST_FILE = f"{VOLUME_PATH}/sample-snlvol"   # your actual file name

print("=== SECRET PROOF ===")
print("Secret value:", MY_SECRET)

print("=== VOLUME PROOF ===")
try:
    files = os.listdir(VOLUME_PATH)
    print("Volume files:", files)
    if TEST_FILE in [f"{VOLUME_PATH}/{f}" for f in files]:
        with open(TEST_FILE) as f:
            print("File content:", f.read().strip())
    else:
        print("Expected file not found in volume")
except Exception as e:
    print("Volume error:", e)

# --- HTTP ENDPOINT ---
@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.get("/secret")
def read_secret():
    return {"secret": MY_SECRET}
