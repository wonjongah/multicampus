f = open("live.txt", "rt", encoding="utf8")
while True:
    text = f.read(10)
    if len(text) == 0: break
    print(text, end='')
f.close()
