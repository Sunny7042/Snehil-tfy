import time
import os

FILE_PATH = "/mnt/data/sampleSnlVol"

print("=== Volume Reader Started ===")

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        content = f.read().strip()
        print("Volume content:", content)
else:
    print("File not found at:", FILE_PATH)

# keep process alive so logs stay
while True:
    time.sleep(3600)




