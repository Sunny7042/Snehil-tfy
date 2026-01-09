import time

FILE_PATH = "/mnt/data/hello.txt"

try:
    with open(FILE_PATH, "r") as f:
        content = f.read().strip()
        print("Volume file content:", content)
except Exception as e:
    print("Failed to read file:", e)

# keep container alive to view logs
while True:
    time.sleep(3600)

