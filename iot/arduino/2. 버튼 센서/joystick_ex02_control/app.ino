#include <Joystick.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>
#include <Servo.h>
#include <Led.h>

Led led(13);
const int SERVO_PIN = 4;
Servo servo;
SimpleTimer timer;
JoyStick joy(A0, A1, 3);
bool mode = true; // true : 주행모드, false : 카메라 방향 모드
LiquidCrystal_I2C lcd(0x27, 16, 2);

// joystick 값 읽고 출력하기
void readJoystick(){
    joystick_value_t value = joy.read();
    char buf[17];

    if(mode){ // 주행모드
        sprintf(buf, "X:%4d/Y:%4d", value.x, value.y);
        lcd.setCursor(0,0);
        lcd.print(buf);
    } else { // 카메라 방향 모드
        servo.write(value.x);
        sprintf(buf, "Angle: %3d", value.x);
        lcd.setCursor(0,1);
        lcd.print(buf);
    }
}
// joystick 운영 모드 변겅
void changeMode(){
    mode = !mode;

    if(mode){ // 주행모드
        joy.setRangeX(-255, 255);
        led.off();
    } else { // 카메라 방향 모드
        joy.setRangeX(0, 180);
        led.on();
    }
}

void setup(){
    lcd.init();
    lcd.backlight();
    lcd.clear();
    servo.attach(SERVO_PIN);
    // DC 모터 : 속도조정은 pwm이용 (0~255), 전진, 후진 : +, -
    joy.setRangeX(-255, 255); 
    joy.setRangeY(-255, 255);
    joy.setCallback(changeMode); // 클릭시 모드가 바뀌면서 값의 범위를
    // 0~180

    led.off();

    timer.setInterval(50, readJoystick);
}

void loop(){
    timer.run();
    joy.check();
}