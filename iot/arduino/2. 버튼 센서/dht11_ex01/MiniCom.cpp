#include "MiniCom.h"

MiniCom::MiniCom() : lcd(0x27, 16, 2) {
}

void MiniCom::init(){
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
}

int MiniCom::setInterval(unsigned long d, timer_callback f){
    return timer.setInterval(d, f);
}

void MiniCom::run(){
    timer.run();
}

void MiniCom::print(int col, int row, const char *pMsg){
    lcd.setCursor(col, row);
    char buf[17];
    sprintf(buf, "%-16s", pMsg); // 이전 긴 문장 덮어쓰기 위해 -16s
    // clear 필요 없어진다
    lcd.print(buf);
}

void MiniCom::print(int row, const char *pMsg){
    print(0, row, pMsg);
    // 한 줄에 문자열 출력
}


void MiniCom::print(int row, const char *pTitle, int value){
    char buf[17];
    sprintf(buf, "%s: %d", pTitle, value);
    print(0, row, buf);
    // 가이드 주면서 정수 출력
}

void MiniCom::print(int row, const char *pTitle, double value, int width){
    char buf[17];
    char temp[14];
    dtostrf(value, width, 2, temp); // 소수점 2자리로 고정
    sprintf(buf, "%s: %s", pTitle, temp);
    print(0, row, buf);
    // 가이드 주면서 실수 출력
}