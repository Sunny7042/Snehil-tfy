import time
import os
import sys

FILE_PATH = "/mnt/data/sample-snlvol"

print("=== Volume Reader Started ===", flush=True)

# small delay so log collector attaches
time.sleep(2)

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        content = f.read().strip()
        print("Volume content:", content, flush=True)
else:
    print("File not found at:", FILE_PATH, flush=True)

# keep alive
while True:
    time.sleep(3600)






