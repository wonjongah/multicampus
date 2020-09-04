def makeHello(message):
     def hello(name):
        print(message + ", " + name)  # 내부함수를 쓸 때 일어나는 현상, 이런 message를 클로저라고 부름

     return hello
enghello = makeHello("Good Morning")
kohello = makeHello("안녕하세요")

enghello("Mr Kim")
kohello("홍길동")