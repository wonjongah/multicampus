def test(numbers):
    numbers[0] = -1
    print(numbers)


def main():
    list1 = [1, 2, 3]
    test(list1)   # numbers = list1과 같다, 호출하는 값이 대입된다...***************
    print(list1)

    
main()


# 콜바이밸류와 결과가 다름 왜??????????
# 다른 메카니즘, 값이 복사가 되는 것이 아니라 참조가 복사가 된다 --> 콜바이레퍼런스
# call by reference -> 원본에 영향을 미친다