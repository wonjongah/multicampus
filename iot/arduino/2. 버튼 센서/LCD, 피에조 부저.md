< lcd_ex01.ino >





\#include <Wire.h>



void setup() {

  Wire.begin();

  Serial.begin(9600);

}



void loop() {

  byte error, address;

  int nDevices = 0;



  Serial.println("Start Scanning...");



  for (address = 1; address < 127; address++) { // 1~256

​    // 1바이트의 의미 없는 데이터를 전송

​    Wire.beginTransmission(address);

​    error = Wire.endTransmission();

​    if (error == 0) {

​      Serial.print("I2C device found at address 0x");

​      if (address < 16) Serial.print("0");

​      Serial.print(address, HEX);  // 16진수

​      Serial.println();

​      nDevices++;

​    }

  }

  if (nDevices == 0)

​    Serial.println("No I2C devices found\n");

  delay(5000); // 5초 후 다시 스캐닝

}





보통은 0x27 주소값 리턴





**lcd 실수 값을 문자열로 변경하기** 

실수를 문자열로 (double을 to string으로 바꾸는 format)

\- char * dtostrf(double __val, signed char __width, unsigned char __prec, char * __s)

 \- __val : 변환할 실수 값

 \- __width : 전체 자리 수 (소수점은 제외)

 \- __prec : 소수점 이하 유효 숫자 수

 \- __s : 변환된 문자열을 저장할 버퍼





F1 -> send text to serial port -> 메시지 입력시 입력한 문자열이 lcd에 출력된다





< lcd_ex04.ino >







\#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {

  Serial.begin(9600);

  lcd.init();

  lcd.setCursor(0, 0);

  lcd.print("Arduino LCD");

  delay(1000);

  lcd.setCursor(0, 1);

  lcd.print("Welcome");

  delay(250);

  // LCD 백라이트 두번 점멸

  lcd.noBacklight();

  delay(250);

  lcd.backlight();

  delay(250);

  lcd.noBacklight();

  delay(250);

  lcd.backlight();

  delay(3000);

  // Open Serial Monitor Type to display 표시

  lcd.clear();

  lcd.setCursor(0, 0);

  lcd.print("Open Serial Mntr");

  lcd.setCursor(0, 1);

  lcd.print("Type to display");

}

// 라인별로 한 줄 전체를 덮어쓰는 형태



String readLine() {

  String line = "";  // 시리얼로 한 줄 입력받아 line 변수에 저장



  while (Serial.available() > 0) {

​    char ch = Serial.read();

​    if (ch != '\r' && ch != '\n') {

​      line += ch;

​    }



  }

  return line;

}



// while(Serial.available() > 0) {

// char ch = Serial.read();

// if(ch != '\r' && ch != '\n')

// lcd.write(ch);

// } 



void loop() {

  if (Serial.available()) {

​    delay(100);

​    // lcd.clear(); // 긴 문장 보내고 -> 짧은 문장 전송

​    lcd.setCursor(0, 0);

​    lcd.print("Message from PC");

​    lcd.setCursor(0, 1);



​    String line = readLine();

​    if (line != "") {  // 수신 데이터 유무

​      lcd.setCursor(0, 1);

​      char buf[17];

​      float d = 3.14159;

​      char buf2[10];

​      dtostrf(d, 5, 3, buf2);

​      sprintf(buf, "%-8s %s", line.c_str(), buf2);  

​      lcd.print(buf);  // const char * 타입



​    }



  }

}







![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfNjIg/MDAxNjAwMjQ5NjU0NTE2.CLgfoeR7TcBDOlPKQ-Gg9jZVwlK0AxNoB5BRypZ4Suog.XzGmZRpKVQPpGXclsyCVFTo4RQdHbYw73LCo-xJXapQg.JPEG.til_t/P20200916_184301044_15F32D3D-C88E-4064-8E50-4A7AFEA2431F.jpg)









< lcd_ex05.ino > -> 5x7 도트 문자 폰트



lcd.createChar(0, happy); // 사용자 문자 저장

lcd.write(0); // 0번 문자 출력







\#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27, 16, 2);

uint8_t smile1[8] = {

  0x00,

  0x11, // B10001

  0x00,

  0x00,

  0x00,

  0x11, // B10001

  0x0E, // B01110

  0x00

};

uint8_t smile2[8] = {

  0x00,

  0x11,

  0x00,

  0x00,

  0x00,

  0x0E,

  0x11,

  0x00

};

void setup() {

  lcd.init();

  lcd.backlight();

  lcd.createChar(0, smile1);

  lcd.createChar(1, smile2);

  lcd.home();

  lcd.write(0);

  lcd.write(1);

}

void loop() {}






![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjU1/MDAxNjAwMjQ5NjU0ODU4.JonguRo2QPjSvm9LLlehmxE_GakpskBQdZsdI1MVboEg.Aga8feSO0ANiIGtbWUaWTsSpoyIfM4qUdnVAapkGrfQg.JPEG.til_t/P20200914_112831295_2E0DBECF-4183-4DFA-A03D-9BAE96D883C4.jpg) 







<clock.ino>





\#include <SimpleTimer.h>

\#include <LiquidCrystal_I2C.h>



LiquidCrystal_I2C lcd(0x27, 16, 2);

SimpleTimer timer;



void printTime(){

  char buf[17];

  unsigned long t = millis();



  // millisecond -> 시:분:초로 변환해서 출력

  int misec = t % 1000 / 100; // 100ms 단위

  t = t / 1000; // 전체 초

  int h = t / 3600;  // 전체 초를 3600(1시간의 초)로 나눈 몫 = 시간

  int m = (t - (h * 3600)) / 60; // 전체 초에서 시간을 빼고 60(1분의 초)로 나눈 몫 = 분

  int s = t - (h * 3600 + m * 60); // 전체 초에서 시간의 초와 분의 초를 빼고 남은 초 = 초



  sprintf(buf, "%02d:%02d:%02d.%d", h, m, s, misec);

  lcd.setCursor(0,0);

  lcd.print(buf);

}



void setup(){

  Serial.begin(9600);

  lcd.init();

  lcd.backlight();



  timer.setInterval(100, printTime); // 100ms 단위로 갱신, 1000을 쓰면 초시계가 된다

}



void loop(){

  timer.run();

}







![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfODYg/MDAxNjAwMjUwNjI3NTQ4.oGb0ABT_23ib2Uwp5ZXvbVnj-CqMz1uxFFhZm3InHPcg.7-taeSSNmtm_Ak2qMzsmFCEx6hyoaWE9RWdx2gsakHAg.JPEG.til_t/P20200916_190238932_041F49DD-64F1-47A6-803F-68FB3E572F23.jpg) 





![img](https://ssl.pstatic.net/static.se2/static/img/alter_video.png) 







**피에조 부저**







![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjkg/MDAxNjAwMjUyODQ2NjIx.f5m3a2Ovoty4FKJhFLXEsSMNL9KOsHFUmItpIQTErqcg.pzkGF0ycFUu5ugIRvgd-GSujaiyc6ougjcEVT6FBZLkg.JPEG.til_t/P20200916_191831696_2D777237-8A0A-48F8-BBDA-8D0490D2F019.jpg) 







﻿Passive Buzzer (수동 부저) 

\- 회로 내장하지 않음

\- 필요한 음역대의 펄스(주파수)를 제공해 멜로디 연주, 전원 인가해서 소리 안 남

\- PWM 이용

\- 후진 엘리제를 위하여 같은 소리 예





Active Buzzer (능동 부저)(스티커 있는 것)

\- 회로 내장형

\- 전원만 인가되면 단일음을 낸다

\- 자동차 후전 소리 같은 예





**빵판의 +를 아두이노의 power의 5V**

**빵판의 -를 아두이노 digital GND**

**패시브부저와 액티브부저의 -부분을 빵판의 -에 꼽고 +가 밑으로 가게 꼽는다**

**나머지 점퍼선으로 빵판의 +와 액티브부저의 +를 연결하면(전원이 들어오면) 소리가 난다**

**(수동으로 소리나게)**

**
**

**
**

![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTI4/MDAxNjAwMjUyODg0MjM3.AAFSwoYllvwfZw_32jtMN3ljYzOdJrh5K3D4QUmUyegg.hPJ8uZauyW43D1MHEOGCpJbXRda2F7U8aU0AwA-z4k4g.JPEG.til_t/P20200916_193207844_4152743E-7685-44F2-AA6C-AE8E6CCD4759.jpg)





< buzzer_ex01.ino>





﻿**빵판의 -와 아두이노 power의 GND에 연결** 

**액티브부저의 +를 digital 5번 핀에 꼽는다**





![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjcx/MDAxNjAwMjUyOTA1Mzg5.V1fKz6mhJAThnOoZDdqb9R-Z4JsQ8HRZ2uTUehCJVskg.19TAfjO1DvoSYfKI1l4p4QKelOkYP-ytPwqKnDNKHPcg.JPEG.til_t/P20200916_193701154_BABBEE51-CEE6-4265-B933-21F2290ED582.jpg)





int buzzerPin = 5;



void setup(){

  pinMode(buzzerPin, OUTPUT);

}



void loop(){

  digitalWrite(buzzerPin, HIGH); // HIGH 소리남

  delay(1000);

  digitalWrite(buzzerPin, LOW);

  delay(1000);

}





LOW의 시간이 짧을 수록 긴박하다는 걸 나타낼 수 있다

거리를 측정하는 초음파와 연계할 수 있다





![img](https://ssl.pstatic.net/static.se2/static/img/alter_video.png)





tone(핀번호, 주파수 [, 기간])



\- 피에조 스피커에 특정 주파수를 발행

\- 비동기 함수

\- 주파수 : unsigned int

\- 기간 : unsigned long

ex) tone(9, 2000, 3000) -> 9000Hz 주파수 소리를 3초간 냄



noTone(핀번호)



\- 피에조 스피커에 주파수 발생 중지





< buzzer_ex02.ino >





int speakerPin = 5;



void setup(){



}



void loop(){

  tone(speakerPin, 5000, 1000);  // 비동기 함수

  delay(2000);  // 1초 소리 + 1초 소리 X

}





< buzzer_ex03.ino > -> 패시브 함수



**digital의 5번에 연결된 선을 패시브의 +와 연결한다**





![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTc1/MDAxNjAwMjUzNzYwNDU0.AVqKL4gt5ZbhKOqkQAYjDAOD9Yk_DYaR7N8zdJLuZKsg.2_HOUGeBe3wQtONrb89AASn8LIwOo21KoWjgQ8j7tOEg.JPEG.til_t/P20200916_195443674_1698FCA3-8168-4A34-B659-053024E7A94D.jpg)







int speakerPin = 5;

int melody[] = {262, 294, 330, 349, 392, 440, 494, 523};



void setup(){

  for(int i = 0; i < 8; i++){

​    tone(speakerPin, melody[i], 250); // 250은 1/4 박자

​    delay(400);

​    noTone(speakerPin);

  }

}



void loop(){

  

}







![img](https://ssl.pstatic.net/static.se2/static/img/alter_video.png) 





< buzzer_ex05.ino > -> 학교종이 땡땡땡을 패시브부저로 연주





\#define C 262

\# define D 294

\# define E 330

\# define _F 349

\# define G 392

\# define A 440

\# define B 494

\# define H 523 

int pzoPin = 5;

int tempo = 200; // 음 재생 시간 설정



int notes[25] = {

  G,

  G,

  A,

  A,

  G,

  G,

  E,

  G,

  G,

  E,

  E,

  D,

  G,

  G,

  A,

  A,

  G,

  G,

  E,

  G,

  E,

  D,

  E,

  C

}



;



void setup() {

  pinMode(pzoPin, OUTPUT);

}



void loop() {

  for (int i = 0; i < 12; i++) {

​    tone(pzoPin, notes[i], tempo);

​    delay(300);

  }

  delay(100);

  for (int i = 12; i < 25; i++) {

​    tone(pzoPin, notes[i], tempo);

​    delay(300);

  }

}







< buzzer_ex06.ino >





\#include <pitches.h>



int speakerPin = 5;

int melody[] = {

  NOTE_C4,

  NOTE_G3,

  NOTE_G3,

  NOTE_A3,

  NOTE_G3,

  0,

  NOTE_B3,

  NOTE_C4,

};

// 음표의 길이 4 = 4분음표(한박자), 8 = 8분 음표(반 박자)

int noteDurations[] = {

  4,

  8,

  8,

  4,

  4,

  4,

  4,

  4

};

void setup() {

  for (int thisNote = 0; thisNote < 8; thisNote++) {

​    int noteDuration = 1000 / noteDurations[thisNote];

​    tone(speakerPin, melody[thisNote], noteDuration);

​    // 음을 구별하기 위해 그 사이에 최소한의 간격을 둔다.

​    int pauseBetweenNotes = noteDuration * 1.30;

​    delay(pauseBetweenNotes);

​    noTone(speakerPin); // 멜로디 멈춤

  }

}

void loop() {}