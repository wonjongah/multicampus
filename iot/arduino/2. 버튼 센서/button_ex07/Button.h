#pragma once
#include <Arduino.h>

class Button{
    protected:
        int pin;
        bool state_previous;
        bool state_current;
        void (*callback)();
    public:
        Button(int pin);
        int read();
        void setCallback(void (*callback)());
        int check();
};