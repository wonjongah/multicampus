#include "Car.hpp" // "" 검색 순서 : cwd(와 include 검색) -> 사용자 lib -> 컴파일러 lib
#include <iostream> // <> 검색 순서 : 사용자 lib -> 컴파일러 lib

// 메서드임을 나타내기 위해 :: 스코프 연산자 쓴다, 어디 소속인지
void Car::setSpeed(int s){
    speed = s;
    // 지역변수 speed X, 멤버변수 speed
}

int Car::getSpeed(){
    return speed;
}
