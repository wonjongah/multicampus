def calcsum(n):
    if n < 0:
        raise ValueError

    total = 0
    for i in range(n+1):
        total += i
    return total

try:
    print("~10 = ", calcsum(10))
    print("~-5 = ", calcsum(-5))
except Exception:
    print("입력값이 잘못되었습니다")