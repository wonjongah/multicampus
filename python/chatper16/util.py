INCH = 2.546

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

print("util", __name__)   # 다른 곳에서 불러오면 __name__이 util로 출력


if __name__ == "__main__":  # 만일 이게 모듈로 다른 데에 임포트가 된다면 밑의 프린트는 작동X
    print("인치 = ", INCH)
    print("합계 = ", calcsum(10))

