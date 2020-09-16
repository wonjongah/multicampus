#pragma once

#include <Arduino.h>
#include <Led.h>

class PWMLed : public Led {
protected:
    int value;

public:
    PWMLed(int pin);

    int getValue();
    void fadeIn(int step=1);    // 점점 밝아지는 것
    void fadeOut(int step=1);   // 점점 어두워지는 것
    void set(int value);
};