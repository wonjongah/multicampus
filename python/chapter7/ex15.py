def calcstep(**args):
    print(args)
    print(type(args))
    # begin = args["begin"]   # args 대신 dict 써도 무방
    begin = args.get("begin", 1)  # 값 없을 때 디폴트 값을 주고 싶다, get()함수!!
    end = args["end"]
    # step = args["step"]
    step = args.get("step", 1)    # end는 필수, 나머지는 옵션이 됐다

    total = 0
    for num in range(begin, end + 1, step):
        total += num

    return total


def main():
    print("3 ~ 5", calcstep(begin=3, end=5, step=1))
    print("3 ~ 5", calcstep(step=1, end=5, begin=3))
    print("3 ~ 5", calcstep(end=5))   # begin = args["begin"]에서 오류, 없는 키에서 접근하려고 함
    #만일  begin 제시하면? 그러나 step 없음...     step = args["step"]에서 종료
    print("3 ~ 5", calcstep(end=10, step=2))


main()