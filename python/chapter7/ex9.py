salerate = 0.9


def kim():
    print("오늘의 할인율:", salerate)  # 읽기 작업, 스택에서 먼저 찾고, 그다음 전역 찾는다


def lee():
    price = 1000
    print("가격:", price * salerate)



kim()
salerate = 1.1    # salerate 바뀜!!!!!!!!!!!!!
lee()