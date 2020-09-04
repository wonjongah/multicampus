def intsum(*ints):
    total = 0
    for num in ints:
        total += num


    return total


print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))