searchword = open("system.log", "r")
for line in searchword:
    if "BEAR" in line:
        print(line)
    if "X-RAY" in line:
        print(line)
searchword.close()
