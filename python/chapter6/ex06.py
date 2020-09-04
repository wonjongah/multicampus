x = 1
gob = 0
while x < 10:
    gob = x * 4
    print("4 X ", x, " = ", gob, sep='')
    x += 1

# -----------------------------------------------------

print()

for x in range(1, 10):
    gob = x * 4
    print("4 X ", x, " = ", gob, sep='')

# -----------------------------------------------------

print()

for dan in range(2, 10):
    print(dan, "단")
    for hang in range(2, 10):
        print(dan, " X ", hang, "=", dan * hang)
