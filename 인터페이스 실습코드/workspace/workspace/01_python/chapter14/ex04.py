f = open("live.txt", "rt", encoding="utf8")
text = ''
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + ":" + row
    line += 1

f.close()
print(text)