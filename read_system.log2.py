search_word = open("/Users/sophie.n/Documents/system.log", "r")
for line in search_word:
    if "BEAR" in line:
        print(line)
    if "X-RAY" in line:
        print(line)
search_word.close()
