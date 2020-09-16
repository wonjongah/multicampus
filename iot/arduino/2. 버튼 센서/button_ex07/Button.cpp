#include "Button.h"


Button::Button(int pin) : pin(pin){
    pinMode(pin, INPUT_PULLUP);
    state_previous = true;
    callback = NULL;
}

int Button::read(){
    return !digitalRead(pin);
    // 풀업이라 반전
}

void Button::setCallback(void (*callback)()) {
    this->callback = callback;
}

int Button::check(){
    state_current = digitalRead(pin);
    if(!state_current) { // 누른 경우
if(state_previous == true) {
    state_previous = false;
    //버튼을 누른 시점에서 해야 할 작업
    // work();
    if(callback != NULL){
    callback();
}
}
delay(5);
} else {
state_previous = true;
}
}