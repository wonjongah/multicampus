#include "PWMLed.h"

PWMLed::PWMLed(int pin) : Led(pin), value(0) {  
    
}

int PWMLed::getValue() {
    return value;
}

// 점점 밝아지는 것
void PWMLed::fadeIn(int step){
    value += step;
    if(value > 255) {
        value = 0;
    }
    analogWrite(pin, value);    
}    

// 점점 어두워지는 것
void PWMLed::fadeOut(int step) {
    value -= step;
    if(value < 0) {
        value = 255;
    }
    analogWrite(pin, value);
} 

// set override
void PWMLed::set(int value) {
    analogWrite(pin, value);
}