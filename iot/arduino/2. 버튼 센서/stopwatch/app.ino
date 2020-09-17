#include <Led.h>

#include <Button.h>

#include <SimpleTimer.h>

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
SimpleTimer timer;
Led led2(3);
Led led3(4);
// Led led3(5);
Button btn1(11); // start, stop
Button btn2(10); // lap time
Button btn3(9); // reset

int timerId = -1; // 스탑워치용 타이머
int blinkTimerId = -1; // 블링크용 타이머

bool state = false; // 0 준비상태, 1 가동상태
unsigned long startTime = 0; // 시작 버튼을 누른 시점
// 기준시간
void printTime(unsigned long t, int row) {
    char buf[17];
    // unsigned long t = millis();

    int misec = t % 1000 / 100; // 100ms 단위
    t = t / 1000;
    int h = t / 3600;
    int m = (t - (h * 3600)) / 60;
    int s = t - (h * 3600 + m * 60);

    sprintf(buf, "%02d:%02d:%02d.%d", h, m, s, misec);
    lcd.setCursor(0, row);
    lcd.print(buf);
}
void printTime() {
    unsigned long t = millis();
    unsigned long diff = t - startTime;
    printTime(diff, 0);
}
void startStop() {
    if (state == false) { // 리셋 이후 처음 버튼을 누른 경우
        // 최초 기동 시작
        startTime = millis(); // 기준 시간 설정
        timer.enable(blinkTimerId);
        led2.off();
        state = true; // 기동중임을 설정
    }
    timer.toggle(timerId);

}

void laptime() {
    if (state) { // 가동중일 때만 출력
        unsigned long t = millis();
        unsigned long diff = t - startTime;
        printTime(diff, 1);
    }
}


void reset() {
    state = false;
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("00:00:00.0");
    led2.on();
    led3.off();
    timer.disable(timerId);
    timer.disable(blinkTimerId);
}

void blink() {
    led3.toggle();
}

void setup() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();

    timerId = timer.setInterval(100, printTime); // 스톱워치용 0.1초 간격으로 호출
    // timerId는 0부터 배정
    // timer.disable(timerId);
    blinkTimerId = timer.setInterval(250, blink); // 아마 1이 될 것
    // 블링크용 0.25초 간격으로 호출
    reset();

    btn1.setCallback(startStop);
    btn2.setCallback(laptime);
    btn3.setCallback(reset);
}

void loop() {
    timer.run();
    btn1.check();
    btn2.check();
    btn3.check();
}