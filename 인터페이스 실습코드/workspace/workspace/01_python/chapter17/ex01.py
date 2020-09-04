nums = [11,22,33]

it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)

