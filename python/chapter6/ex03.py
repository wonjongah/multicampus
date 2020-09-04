for a in range(5):  # 시작값을 입력하지 않았을 때는 디폴트 0부터 시작
    print("이 문장을 반복합니다")


for x in range(1, 51):
    if x % 10 == 0:
        print("+", end='')
    else:
        print("-", end='')