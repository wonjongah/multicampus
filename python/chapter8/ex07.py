def main():
    s = "Good morning. my love KIM"

    print(s.lower())     # 바뀐 값을 리턴
    print(s.upper())
    print(s.swapcase())
    print(s.capitalize())
    print(s.title())
    print(s)     # 원본 그대로 있음
    print(s[::-1])  # 원본 리버스하는 게 아니라 리버스된 문자열을 리턴

    s = "     angel"
    print(s + "님")
    print(s.strip() + "님")
    print(s.lstrip() + "님")
    print(s.rstrip() + "님")


main()