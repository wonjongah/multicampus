class Outer:
 def __init__(self, func):
    self.func = func

 def __call__(self):   # 객체의 인스턴스를 함수호출하듯 사용했을 때 이 메소드 호출
     print("-"*20)
     self.func()
     print("-"*20)

def inner():
 print("결과를 출력합니다.")

inner = Outer(inner)  #함수였던 이너가 객체가 됐다
inner()  # 모양은 함수호출이나 실제변수는 객체