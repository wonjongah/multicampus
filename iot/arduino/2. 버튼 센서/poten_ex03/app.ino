#include <PWMLed.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>
#include <AnalogSensor.h>

PWMLed led(3);

const int potentiometerPin = A0;

int potentiometerValue;
int brightness;

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup(){
    lcd.init();
    lcd.backlight();
    lcd.clear();
    Serial.begin(9600);
}

void loop(){
    char buf[17];

    potentiometerValue = analogRead(potentiometerPin);

    sprintf(buf, "org : %4d", potentiometerValue);
    lcd.setCursor(0,0);
    lcd.print(buf);
    
    // brightness = map(potentiometerValue, 0, 1023, 0, 255);
    brightness = map(potentiometerValue, 0, 1023, 255, 0);

    sprintf(buf, "bright : %4d", brightness);
    lcd.setCursor(0, 1);
    lcd.print(buf);

    led.set(brightness);
}
