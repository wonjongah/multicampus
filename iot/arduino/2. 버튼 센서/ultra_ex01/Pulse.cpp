#include "Pulse.h"

Pulse::Pulse(int onDelay, int offDelay)
: onDelay(onDelay), offDelay(offDelay){

    value = HIGH;
    state = false;
    callback = NULL; // null 초기화
    oldTime = millis(); // 현재 시간   
}

void Pulse::setDelay(int onDelay, int offDelay){
    this->onDelay = onDelay;
    this->offDelay = offDelay;
} // distance 바뀔 때 온은 그대로 두고 오프를 조정하면 된다

void Pulse::play(){ // 운영 시작
    state = true;
    value = HIGH;
    oldTime = millis();
}

void Pulse::stop(){ // 운영 정지
    state = false;
    value = LOW;
}

void Pulse::run(){
    if(!state) return; // state가 false이면 그냥 리턴해버림, 운영 안 함

    unsigned long currentTime = millis();
    unsigned long diff = currentTime - oldTime;
    
    long interval = value ? onDelay : offDelay; // value가 트루면 on 폴스면 off

    if(diff >= interval) // 시간이 다 되었으면
    {
        // 엣지트리거, 상승, 하강 (값이 바뀔 때)
        oldTime = currentTime;
        value = !value; 
        if(callback!=NULL){
            callback(value);
        }
    }
} // 시간 측정해서 하이가 되야 할 지 로우가 되어야 할 지 