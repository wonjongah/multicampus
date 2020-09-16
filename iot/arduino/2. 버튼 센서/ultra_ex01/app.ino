#include <MiniCom.h>
#include "Ultra.h"

MiniCom com;

Ultra ultra(2, 3);
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
}
void setup(){
    com.init();
    com.setInterval(1000, checkDistance);
}

void loop(){

    com.run();
}