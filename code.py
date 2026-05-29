import time
import os

num=0
openai_key = os.environ.get("OPENAI_API_KEY")

while True:
    print(f"{num}: {openai_key}")
    num += 10
    time.sleep(10)
