for x in range(9, 0, -1):
    print(" " * x, sep="", end="")
    for y in range(((10 - x) * 2 - 1)):
        print("*", sep="", end="")
    print()