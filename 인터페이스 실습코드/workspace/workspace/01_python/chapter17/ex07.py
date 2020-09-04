def inner():
 print("결과를 출력합니다.")

def outer(func):
    def wrapper():
     print("-"*20)
     func()
     print("-"*20)
    return wrapper

inner = outer(inner)  # 매개변수로 실제 해야 할 함수 전달.. 아까는 메시지였던 게 지금은 함수
# inner 바뀜... 기존코드 버린 게 아님.. 덧붙임
inner()
