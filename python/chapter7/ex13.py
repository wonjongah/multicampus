def int_sum(*numbers):  # 가변 인수,
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    return total



def main():
    print(int_sum(1, 2, 3, 4, 5))
    print(int_sum())  # 루프 돌지 않음, 가변인수 값 없음



main()