#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup(){
    lcd.init(); // LCD 초기화
    lcd.backlight(); // 백라이트 켜기
    lcd.setCursor(3, 0);  // 커서 위치 설정 (x,y)

    // 문자열 출력
    lcd.print("Hello, World!");
}

void loop(){

}