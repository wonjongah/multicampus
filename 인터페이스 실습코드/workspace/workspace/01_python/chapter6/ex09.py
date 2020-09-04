for x in range(9, 0, -1):
    print(" " * x, sep='', end='')
    for y in range(10-x):
        print("*", sep='', end='')
    print()

print()

for x in range(9, 0, -1):
    print(" " * x, sep='', end='')
    print("*" * (10 - x), sep='', end='')
    print()