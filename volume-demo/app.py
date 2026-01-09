import time
import os

FILE_PATH = "/mnt/data/sampleSnlVol"

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        print("Volume content:", f.read().strip())
else:
    print("File not found in volume!")

while True:
    time.sleep(3600)  # keep pod alive for logs



