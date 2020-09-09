from pathlib import Path

p = Path("system.log")
contents = p.read_text().splitlines()

for line in contents:
    if "BEAR" in line:
        print(line)
    if "X-RAY" in line:
        print(line)
