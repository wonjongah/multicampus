#컴퓨터와 나와 가위바위보 누가 이겼느냐
#주먹 0 가위 1 보 2
import random


ROCK = 0
SCISSORS = 1
PAPER = 2
count = 0
comwin = 0
mewin = 0
for num in range(3):
        # com = int(10 * random.random()) % 3

        com = int(random.random() * 3)
        # (0~1] * 3 -> (0~3]

        me = int(input("0:주먹, 1:가위, 2:보 :"))
        print(count + 1, "번째는 ", sep='', end='')
        if com == me:
            print("비겼습니다")
        elif com == ROCK:
            if me == SCISSORS:
                print("컴퓨터가 이겼습니다")
                comwin += 1
            else:
                print("내가 이겼습니다")
                mewin += 1
        elif com == SCISSORS:
            if me == ROCK:
                print("내가 이겼습니다")
                mewin += 1
            else:
                print("컴퓨터가 이겼습니다")
                comwin += 1
        elif com == PAPER:
            if me == ROCK:
                print("컴퓨터가 이겼습니다")
                comwin += 1
            else:
                print("내가 이겼습니다")
                mewin += 1
        count += 1

print(comwin, "대", mewin, "으로 ", sep="", end="")
if (comwin > mewin):
    print("컴퓨터가 이겼습니다")
elif (comwin < mewin):
    print("내가 이겼습니다")
else:
    print("비겼습니다")
# 변할 확률이 있는 변수와 변할 확률이 없는 변수
# 대문자와 소문자, 상수와 변수
# 파이썬에는 상수 선언이 없음.. 내가 변수를 상수처럼 써야 함

