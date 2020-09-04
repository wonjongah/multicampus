for x in range(9, -1, -1):
    print(" " * x, sep='', end='')
    for y in range(1, 10, -1):
        print("*" * y,sep='', end='')
    print()