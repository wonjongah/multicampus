#include <SimpleTimer.h>

SimpleTimer timer;
int pin_LED1 = 4;
int pin_LED2 = 3;
int pin_button = 11;
boolean LED_state = false;

// 모든 C++의 함수명의 의미 -> 함수 시작주소를 가지고 있는 포인터 상수

void blink() {
    LED_state = !LED_state;
    digitalWrite(pin_LED1, LED_state);
}

void setup() {
    pinMode(pin_LED1, OUTPUT);
    digitalWrite(pin_LED1, LED_state);
    pinMode(pin_LED2, OUTPUT);
    digitalWrite(pin_LED2, false);

    pinMode(pin_button, INPUT_PULLUP);
    timer.setInterval(1000, blink); // 함수의 주소 넘긴 것, 함수를 매개변수로 전달 (blink)

}

void loop() {
    timer.run(); // 타이머 운영
    // 버튼 상태를 읽어서 13번 핀에 연결된 LED에 표시
    digitalWrite(pin_LED2, !digitalRead(pin_button));
}