import os
import time

# Mounted secret path based on your YAML + UI
SECRET_PATH = "/var/secrets/snehil-serv/password"

# Default fallback
MY_SECRET = "SECRET_NOT_FOUND"

# Read secret from mounted file
if os.path.exists(SECRET_PATH):
    with open(SECRET_PATH, "r") as f:
        MY_SECRET = f.read().strip()

# Print secret to logs (TrueFoundry captures stdout)
print("Secret value:", MY_SECRET)

# Keep container running so logs don’t exit immediately
while True:
    time.sleep(3600)
