import time
import os

FILE_PATH = "/mnt/data/sample-snlvol"

print("=== Volume Reader Started ===")

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        content = f.read().strip()
        print("Volume content:", content)
else:
    print("File not found at:", FILE_PATH)

while True:
    time.sleep(3600)





