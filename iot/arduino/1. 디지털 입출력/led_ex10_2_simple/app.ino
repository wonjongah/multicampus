#include <SimpleTimer.h>

int pin_LED1 = 3;
int pin_LED2 = 7;
int pin_LED3 = 13;

SimpleTimer timer; // 정적할당, 전역영역에 할당

void blink_1000(){
    int state = digitalRead(pin_LED1); // 이 핀의 현재 상태
    digitalWrite(pin_LED1, !state);
}

void blink_500(){
    int state = digitalRead(pin_LED2);
    digitalWrite(pin_LED2, !state);
}

void blink_300(){
    int state = digitalRead(pin_LED3);
    digitalWrite(pin_LED3, !state);
}
void setup(){
    pinMode(pin_LED1, OUTPUT);
    pinMode(pin_LED2, OUTPUT);
    pinMode(pin_LED3, OUTPUT);
    timer.setInterval(1000, blink_1000);
    timer.setInterval(500, blink_500);
    timer.setInterval(300, blink_300);
}

void loop(){
    timer.run();
}