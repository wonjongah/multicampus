def main():
    s = "독도는 일본땅. 대마도도일본땅"
    print(s)
    print(s.replace("일본", "한국"))
    print(s)    # 원본은 수정불가

    message = "안녕하세요"
    print(message.center(30))
    print(message.ljust(30))
    print(message.rjust(30))

    trabler = """
    강나루 건너서
    밀밭 길을
    
    구름에 달 가듯이
    가는 나그네
    """

    poet = trabler.splitlines()
    for line in poet:
        print(line.center(30))


main()