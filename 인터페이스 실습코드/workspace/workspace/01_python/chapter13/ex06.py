def test(str):  # test 함수만 봐서는 에러가 날 지 안 날 지 모름, 날 가능성은 있으나
    score = int(str)  # 점을 int로 변환하지 못함
    print(score)

def work():  # work와 work2에서는 에러가 났는지 알 수 있나.. 함수 사용하는 쪽에서 에러처리
    str = "89점"
    try:
        test(str)
    except Exception as e:  # 모든 에러 커버
        print(e)

    print("작업완료")

def work2():
    str = "89"
    test(str)
    # 출력만 보고는 어떤 함수가 잘못한 지는 모름....work()가 잘못했는데


def main():
    work()


main()