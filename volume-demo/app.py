import time
import os

FILE_PATH = "/mnt/data/samplesInVol"

print("🔍 Checking volume file...")

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        content = f.read().strip()
        print("📦 Volume file content:", content)
else:
    print("❌ File not found at:", FILE_PATH)

# keep container alive
while True:
    time.sleep(3600)


