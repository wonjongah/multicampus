#include "Led.h"

#include <SimpleTimer.h>

SimpleTimer timer;
// int pin_button = 11;
// int led = 4;
Led led1(3);
Led led2(4);
Led led3(5);
Button btn1(9);
Button btn2(10);
Button btn3(11);

bool blinkPlay = false; // 블링크 중인지 여부, 디폴트는 중지
int blinkTimer = -1; // 블링크용 타이머 id

// boolean state_previous = true;
// boolean state_current;
// int count = 0;
void led2OnOff() {
    led2.toggle();
}

void led3Blink() {
    led3.toggle();
}

void led3BlinkControl() {
    blinkPlay = !blinkPlay; // 상태반전
    if (!blinkPlay) { // 이제 블링크 중지면
        led3.off();
    }
    timer.toggle(blinkTimer); // 타이머 활성/비활성 토글
}
void setup() {
    Serial.begin(9600);
    // pinMode(pin_button, INPUT_PULLUP);
    // pinMode(led, OUTPUT);
    btn2.setCallback(led2OnOff);
    btn3.setCallback(led3BlinkControl);
    blinkTimer = timer.setInterval(500, led3Blink);
    timer.disable(blinkTimer); // 타이머 중지 상태로 시작
}

void work() {
    led1.toggle();
    // int ledState = digitalRead(led);
    // digitalWrite(led, !ledState);
    // count++;
    // Serial.println(count);
}


void loop() {
    // led.set(btn.read()); // 풀업버튼인 경우 반전
    timer.run();
    led1.set(btn1.read());
    btn2.check();
    btn3.check(); // 에지(falling)이 발생했는지 체크
    // state_current = digitalRead(pin_button);
    // led.set(!state_current);
    // if(!state_current) { // 누른 경우
    // if(state_previous == true) {
    //     state_previous = false;
    //     //버튼을 누른 시점에서 해야 할 작업
    //     work();

    // }
    // delay(5);
    // } else {
    // state_previous = true;
    // }
}

