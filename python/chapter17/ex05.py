def calc(op, a, b): # 함수의 인자로 전달할 수 있다.
    op(a, b)

def add(a, b):
    print(a + b)

def multi(a, b):
    print(a * b)

calc(add, 1, 2)
calc(multi, 3, 4)
