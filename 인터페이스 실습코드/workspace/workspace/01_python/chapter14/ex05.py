f = open("live.txt", "rt", encoding="utf8")
rows = f.readlines()

for no, s in enumerate(rows, 1):
    print(f"{no} : {s}", end='')

f.close()