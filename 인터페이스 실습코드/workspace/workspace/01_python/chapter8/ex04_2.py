import random

def rand(start, end):
    return int(random.random() * (end - start +1)) + start # +1하면 뒤 숫자 포함
    #return number


def main():
    num = rand(1, 100)
    count = 0
    flag = False
    for i in range(5): # for i in range(1, 6):  num = int(input(str(i) + "번쩨 추측값:"))
        print(count + 1, end="")
        int1= int(input("번째 추측값 : "))
        count += 1    # result = number - num 해서 리절트와 0을 비교해서 답 찾기
        if int1> num: # 빼기로 비교하면 플래그 안 세워도 된다
            print(int1, "보다 작습니다")
            continue
        elif int1 < num:
            print(int1, "보다 큽니다")
            continue
        else:
            print("정답입니다")
            flag = True
            break
    if flag == False:
        print("실패했습니다")

main()