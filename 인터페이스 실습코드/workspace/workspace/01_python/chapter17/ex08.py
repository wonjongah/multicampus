def outer(func):
 def wrapper():
    print("-"*20)
    func()
    print("-"*20)
 return wrapper
@outer # outer의 리턴값을 호출하는 것 <= inner = outer(inner)
def inner():
 print("결과를 출력합니다.")

inner()
