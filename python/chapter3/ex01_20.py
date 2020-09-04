#컴퓨터와 나와 가위바위보 누가 이겼느냐
#주먹 0 가위 1 보 2
import random

com = 0
me = 1

if com == 0:
    if me == 0:
        print("비겼습니다")
    if me == 1:
        print("컴퓨터가 이겼습니다")
    if me == 2:
        print("내가 이겼습니다")
elif com == 1:
    if me == 0:
        print("내가 이겼습니다")
    if me == 1:
        print("비겼습니다")
    if me == 2:
        print("컴퓨터가 이겼습니다")
elif com == 2:
    if me == 0:
        print("컴퓨터가 이겼습니다")
    if me == 1:
        print("내가 이겼습니다")
    if me == 2:
        print("비겼습니다")

# if com == me: print("비겼습니다") --> 세 개의 케이스가 처리된다
# elif com == 0:
# if me == 1: print("컴퓨터가 이겼습니다")
# else: print("내가 이겼습니다")
# 나와 컴퓨터가 같으면 비긴다를 먼저 적어두고 나머지를 컴퓨터를 기준 잡아서 나머지 거르기
# 경우의 수를 찾고 적은 코드로 할 수 있는 것은 거르기
# 그러나 유지보수 측면에서 좋은 코드는 아니다, 그렇기 때문에 주석을 단다, 하지만 이것도 좋은 코드가 아니래 ㅜㅜ\
# 코드 값을 그대로 쓰면 사람에게는 별로 좋지 않음, 알아보기 힘들다, 바로 눈으로 이해할 수 있는 무언가로 대치
# 변수명을 이용!! --> 가독성 좋은 코드


ROCK = 0
SCISSORS = 1
PAPER = 2

com = int(10 * random.random()) % 3

# random.random() --> 0과 1 사이의 실수를 리턴함
# 하지만 우리가 원하는 것은 0에서 2 사이의 정수를 원함
# 곱하기 10을 하면 0에서 10미만까지 실수가 나옴, 거기에 int를 걸면 0에서 9까지 정수가 나온다
# 나머지 연산, 3으로 연산하면 나머지는 무조건 0, 1, 2에서 나온다!!
com = int(random.random() * 3)
# (0~1] * 3 -> (0~3]

me = int(input("0:주먹, 1:가위, 2:보 :"))

if com == me:
    print("비겼습니다")
elif com == ROCK:
    if me == SCISSORS:
        print("컴퓨터가 이겼습니다")
    else:
        print("내가 이겼습니다")
elif com == SCISSORS:
    if me == ROCK:
        print("내가 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
elif com == PAPER:
    if me == ROCK:
        print("컴퓨터가 이겼씁니다")
    else:
        print("내가 이겼습니다")

# 변할 확률이 있는 변수와 변할 확률이 없는 변수
# 대문자와 소문자, 상수와 변수
# 파이썬에는 상수 선언이 없음.. 내가 변수를 상수처럼 써야 함

