def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
    print("~", n, "=", total)
# 단일 책임의 원칙에 위배
# 연산과 출력 동시에, 출력을 다르게 하고 싶을 때 불리

printsum(4)
printsum(10)

print()

a = printsum(4)   #리턴값 없는 함수... None
print(a)

