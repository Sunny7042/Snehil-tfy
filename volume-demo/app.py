import os
import time

MOUNT = "/mnt/data"

print("Listing contents of /mnt/data:", flush=True)
time.sleep(2)

try:
    print(os.listdir(MOUNT), flush=True)
except Exception as e:
    print("Error listing volume:", e, flush=True)

while True:
    time.sleep(3600)







