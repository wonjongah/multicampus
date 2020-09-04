from util import *   # from util import INCH, calcsum (이게 권장!!!!!!!!!!!)
                     # import가 되면 import된 모듈 한 번 실행한 뒤에 자기 코드 실행
                     # 즉 util 코드 먼저 실행되고 밑의 코드 실행
print("1inch = ", INCH)
print("~10 = ", calcsum(10))

if __name__ == '__main__':
    print("wolrd")