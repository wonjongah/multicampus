def main():
    str = "89"
    try:
        score = int(str)
        print(score)
        a = str[5]  # 인덱스 벗어남 0 1 밖에 없는데
    except (ValueError, IndexError):
        print("점수의 형식이나 첨자가 잘못되었습니다")

    print("작업완료")


main()