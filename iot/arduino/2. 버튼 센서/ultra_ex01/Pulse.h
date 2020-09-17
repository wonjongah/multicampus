#pragma once

#include <Arduino.h>

typedef void (*pulse_callback_t)(int); // pulse_callback_t이 타입이 된 것

class Pulse{
    protected:
        int onDelay; // HIGH 시간
        int offDelay; // LOW 시간

        int value; // 현재 상태값 (H/L)
        unsigned long oldTime; // 최근의 상태 변경 시점 기록

        bool state; // 항상 pulse운영하지 않고, 일정 값 이상이면 운영
        pulse_callback_t callback;

    public:
        Pulse(int onDelay, int offDelay);

        void setDelay(int onDelay, int offDelay);
        void run();
        int read() {return value;}

        bool getState() {return state;} 
        void play();
        void stop();

        void setCallback(pulse_callback_t callback){this->callback = callback;}

};