#pragma once

#include <string>
using namespace std;

// 헤더 파일
// 클래스 원형
class Car {
// 디폴트 접근 제한자 : private
    int speed;
    int gear;
    string color;

public:
    
    int getSpeed(); // 함수 원형
    void setSpeed(int s);
};

