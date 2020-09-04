try:
    f = open("test1/t.txt", "rt", encoding="utf8")  # 파일명에 없는 파일이면 오류, 프로그램 실행될 당시의 디렉토리 중요
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다")
finally:
    f.close()  # 오픈에 오류나면 오픈한 적이 없음, 오픈에 에러 -> f는 존재하지 않음..  f라는 변수 자체가 없는 것
