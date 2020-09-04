def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index : index+2]  # 함수가 끝나면 SropIteration 던짐
        # yield , 변수의 마지막 값과 상태를 저장하게 된다
        # 그렇게 변환하라~ yield

solarterm = seqgen("입춘우수경친춘분청명곡우입하소만망종하지소서대서")
# seqgen 형식적으론 함수 호출,, 리턴 없는데? 그럼 solarterm은 뭐냐?
# 모르면 print()로 찍어보기
print(solarterm)  # 객체다!! 그 함수 실행하겠단 이야기가 아님~
# yield 함수 호출하는 행위는 이걸 실행하겠다는 행위가 아니라 변환하겠다는 말
# 객체 정의 구문이 복잡하니까 그냥 함수 형식으로 표현하면 파이썬이 그 함수가 호출될 때 iter와 next를 가지는
# 객체로 변환시켜주고, 그 객체의 넥스트의 코드를 yield 이후의 코드로 채워주는 것
# 제너레이트 실행시키면 iter next 가지는 객체를 저절로 만들어주는 것

for k in solarterm:
    print(k, end=",")