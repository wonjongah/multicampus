def list.sort(key= None, reverse= False)

    ...




list.sort(key=lambda x: x[1])

# --------------------------------------------------

key = [1,2,3]

def test(key):  # 위는 전역변수 키, test 안에 키는 함수 실행될 때 스택에,, 지역변수

    ...

test(key= key)   # 왼쪽키는 인수의 이름, 오른쪽은 값 (전역변수 키)