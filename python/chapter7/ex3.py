def calcrange(begin, end):
    total = 0;

    for num in range(begin, end+1):
        total += num
    return total


print("3 ~ 7 =", calcrange(3, 7))