import random

def rand(start, end):
    return int(random.random() * (end - start +1)) + start # +1하면 뒤 숫자 포함
    #return number


def main():   # entry point
    start = 1
    end = 6
    for i in range(5):
        num = rand(start, end)
        print(num)
main()