#include <MiniCom.h>
#include <Ultra.h>
#include <Led.h>
#include <Servo.h>
#include "Pulse.h"

MiniCom com;
Led led(8);
Ultra ultra(2, 3);
Servo servo;
Pulse pulse(100, 500);

int delayTimes[] = {
    50, 100, 200, 500, 1000
}; // ms, 다섯 단계로 나누어 간격을 나눔

void pulseCallback(int value){
    // led 제어
    led.set(value);
    // value가 트루면 켜지고 폴스면 꺼진다
}

// int echoPin = 2;
// int triggerPin = 3;

void checkDistance(){
    // trigger 핀으로 10ms의 펄스를 발생
    // digitalWrite(triggerPin, HIGH);
    // delayMicroseconds(10);
    // digitalWrite(triggerPin, LOW);

    // // echo 핀 입력으로부터 거리를 cm 단위로 계산
    // int distance = pulseIn(echoPin, HIGH) / 58;

    int distance = ultra.read();
    com.print(0, "distance", distance);
    if(distance < 10){
        // led.on(); /
        // pulse의 offdelay를 distance를 고려하여 조정
        // int offDelay = map(distance, 0, 9, 50, 1000); // 거리에 따라 딜레이타임을 균등하게 나눔
        int offDelay = map(distance, 0, 9, 0, 4); // 0~4는 delayTimes의 개수
        // 균등하게 말고 가까이 있을 때는 짧게, 멀리 있을 때는 delayTime을 크게
        // offDelay는 delayTimes의 인덱스
        pulse.setDelay(10, delayTimes[offDelay]); // high의 값을 10으로 고정, low의 값을 distance에 따라 조정
        // 근접하면 offdelay 작아지고, 멀어지면 offdelay 커질 것
        servo.write(90);
        if(!pulse.getState()){ // 처음 10cm 이하로 들어왔을 때
            pulse.play();
        }
    } else {
        if(pulse.getState()){
            pulse.stop();
        }
        // led.off();
        servo.write(0);
    }
}
void setup(){
    com.init();
    servo.attach(9);
    servo.write(0);
    pulse.setCallback(pulseCallback);
    com.setInterval(1000, checkDistance);
}

void loop(){
    com.run();
    pulse.run(); // false or true에 따라서 운영하거나 안 하거나
}

