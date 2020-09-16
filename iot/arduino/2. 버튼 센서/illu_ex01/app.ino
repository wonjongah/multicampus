#include <AnalogSensor.h>
#include <Led.h>
#include <LiquidCrystal_I2C.h>
#include <PWMLed.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
// int pSensor = A0;
// int ledPin = 3;
AnalogSensor pSensor(A0, 0, 1023); // 범위 조정 가능
// Led led(3);
PWMLed led(3);

void setup() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
    led.off();
    // pinMode(ledPin, OUTPUT);
}

void printIllu(int value){
    char buf[17];
    sprintf(buf, "Read Value : %3d", value);
    lcd.setCursor(0,0);
    lcd.print(buf);
}
void loop() {
    // int readVal = analogRead(pSensor);
    int readVal = pSensor.read();
    readVal = constrain(readVal, 0, 200);
    // Serial.print("Read Value = ");
    // Serial.println(readVal);
    int brightness = map(readVal, 0, 200, 255, 0);
    // readVal이 높으면(밝으면), led가 꺼지고, readVal이 낮으면 led 켜지고
    printIllu(readVal);
    led.set(brightness);
    // if(readVal < 15) { // 어두워지면 LED 켜기
    //     // digitalWrite(ledPin, HIGH);
    //     led.on();
    // } else {
    //     // digitalWrite(ledPin, LOW);
    //     led.off();
    // }
    delay(200);
    }