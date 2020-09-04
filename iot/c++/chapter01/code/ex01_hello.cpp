#include <iostream>
// # 붙으면 c++에선 추상의미 전처리를 하라! preprocessing
// <iostream> 모듈! 인클루드가 파이썬에서 쓰는 용어로 import 
// 입출력과 관련된 모듈(c++에선 라이브러리라고 부름)

using namespace std;
// standard 표준 의미
// 기본으로 namespace std로 쓰겠다

int main(int argc, char const *argv[]) // 괄호에 매개변수 있으면 함수
// 파이썬에선 def, c++에선 바로 함수 명을 이용해서 정의내림
// 데이터타입을 사전에 명시해줘야 함, 정의한 데이터타입만 사용할 수 있음
//함수의 리턴타입도 명시해줘야 함 -> 지금 보는 데에선 int
// 변수도 데이터 타입 명시해줘야 함
{ // 파이썬에선 코드블럭을 들여쓰기로 했지만 c++에선 중괄호{} 이용해서 코드블럭 지정
    cout << "Hello I am Jonga" << endl;
    // cout(console out), 데이터의 값을 출력할 때 사용하는 객체
    // << -> 데이터 전송하겠다 그 옆에 전송할 데이터 적어준다
    // 이 데이터를 cout으로 보내라(왼쪽객체에게)
    // 또 전송할 데이터가 있다면 <<를 또 쓰면 된다
    // endl -> 줄 바꾸는 상수
    std::cout << "Hello I am Jonga" << std::endl << "종아";
    // cout의 사용법은 두 가지
    // cout은 std라는 namespace에 정의되어 있음, using문 안 써줬다면 이렇게 적어줘야 함
    return 0;
    // int로 리턴한다고 했으니! 데이터타입 일치해야 함
    // 이 함수의 실행을 끝내겠다는 의미로 리턴
}

// 모든 언어에서는 이름충돌이 생기기 마련이다
// c++에선 namespace로 이름충돌 다룬다
// cout이라는 식별자는 std의 범주 아래 정의하고 있는 것
// std::cout -> 다른::cout이 아니라 std에서 정의한 cout이다

// 코드러너로 실행 -> ctrl + alt + N

// ex01_hello.cpp:16:5: error: 'cout' was not declared in this scope
// using namespace 안 쓰면 생기는 오류, cout이 어디 소속인지 모르겠다

// 코드를 실행하면 .exe라는 실행파일이 생긴다
// 파이썬과 c++ 차이, 파이썬은 소스를 매번 파이썬이 실행시키는 방식
// c++은 컴파일해서 .exe를 만들어준다
