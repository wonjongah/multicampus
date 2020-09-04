def comm():

    try:
        print("네트워크 접속")
        d = 0
        if d != 0:
            return # 더이상 진행 못 해 끝내야 해
        a = 2 / d
        print("네트워크 통신 수행")
    except:
        pass  # 코드블럭 필요한데 채울 내용 없을 때
    finally:
        print("접속해제")  # 닫는 역할!~!

   # print("접속해제")
    print("작업 완료")

def main():
    comm()

# except pass쓰면 되지 왜 finally 씀? -> 제대로 클린업 안 됐다
# 클린업, 어떠한 메카니즘이든 트라이 블럭 벗어나면 파이널리 실행하고 리턴해라
# 네트워크, 파일 오픈 클로즈 꼭!
main()