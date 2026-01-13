from fastapi import FastAPI
import os

app = FastAPI()

SECRET = os.getenv("MY_SECRET", "SECRET_NOT_FOUND")
VOLUME_PATH = "/mnt/data"

print("==== SERVICE STARTED ====")
print("Secret:", SECRET)

print("Volume listing:")
try:
    print(os.listdir(VOLUME_PATH))
except Exception as e:
    print("Volume read error:", e)


@app.get("/")
def hello():
    return {"message": "Service running successfully"}

