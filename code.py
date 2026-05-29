import os, sys, time

num = 0
print(f"PID: {os.getpid()}, PPID: {os.getppid()}")
print(f"Executable: {sys.executable}")
print(f"OPENAI_API_KEY in os.environ: {'OPENAI_API_KEY' in os.environ}")
print(f"Environ keys: {sorted(os.environ.keys())}")
openai_key = os.environ.get("OPENAI_API_KEY")

while True:
  print(f"{num}: {openai_key}")
  num += 10
  time.sleep(10)
