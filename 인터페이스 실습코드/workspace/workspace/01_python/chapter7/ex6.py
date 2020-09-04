def calcstep(begin, end, step = 1):   # 비긴, 엔드는 필수요소, 스텝은 필수요소 아님
    total = 0                         # 스텝은 인수 없으면 1, 있으면 그거 씀
    for num in range(begin, end + 1, step):
        total += num


    return total


print("1~10 = ", calcstep(1, 10, 2))
print("2~10 = ", calcstep(1, 100))