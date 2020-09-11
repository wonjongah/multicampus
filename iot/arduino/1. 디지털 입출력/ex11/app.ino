#include <SimpleTimer.h>

int pin_LED1 = 13;
int pin_LED2 = 3;
boolean LED_state1 = false;
boolean LED_state2 = false;
unsigned long time_p1, time_c1;
unsigned long time_p2, time_c2;
unsigned long count = 0;

void setup(){
    pinMode(pin_LED1, OUTPUT);
    pinMode(pin_LED2, OUTPUT);
    digitalWrite(pin_LED1, LED_state1);
    digitalWrite(pin_LED2, LED_state2);
    Serial.begin(9600);
    time_p1 = millis();
    time_p2 = millis();
}

void loop(){
    blink_1000();
    blink_500();
}

void blink_1000(){
    time_c1 = millis();
    if(time_c1 - time_p1 >= 1000){
        time_p1 = time_c1;
        LED_state1 =! LED_state1;
        digitalWrite(pin_LED1, LED_state1);
    }
}

void blink_500(){
    time_c2 = millis();
    if(time_c2 - time_p2 >= 500){
        time_p2 = time_c2;
        LED_state2 =! LED_state2;
        digitalWrite(pin_LED2, LED_state2);
    }
}