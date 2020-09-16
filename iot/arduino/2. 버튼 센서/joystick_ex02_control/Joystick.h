#pragma once

#include <Arduino.h>
#include <AnalogSensor.h>
#include <Button.h>

struct joystick_value_t
{
    int x;
    int y;
    int z;
} value; // 복합 데이터 표현하는 방법

// class JoystickValue{
// public:
//     int x;
//     int y;
//     int z;
    
//     생성자();
// };

class JoyStick{
    protected: // private는 상속이 안 된다
    AnalogSensor jX;
    AnalogSensor jY;
    Button btn;

    public:
    JoyStick(int x, int y, int z);
    // Joystick(Joystick &other); // 복사 생성자 매개변수로 자기자신과 다른 녀석

    int readX();
    int readY();
    void setRangeX(int toMin, int toMax);
    void setRangeY(int toMin, int toMax);

    int readZ(); // 버튼의 상태 읽기
    void setCallback(button_callback_t callback);
    void check();

    joystick_value_t read(); // 한번 호출에 값 세 개 다 얻고 싶다
    // 파이썬에서는 리스트, 튜플 이용

};