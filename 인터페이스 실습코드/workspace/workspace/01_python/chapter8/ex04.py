import random

def rand(start, end):
    return int(random.random() * (end - start +1)) + start # +1하면 뒤 숫자 포함
    #return number


def main():
    num = rand(1, 100)
    count = 0
    while True:
        print(count + 1, end="")
        int1= int(input("번째 추측값 : "))
        count += 1
        if int1> num:
            print(int1, "보다 작습니다")
            continue
        elif int1 < num:
            print(int1, "보다 큽니다")
            continue
        else:
            print("정답입니다")
            break

main()