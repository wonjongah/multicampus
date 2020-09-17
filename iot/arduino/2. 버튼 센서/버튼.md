 ![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfNTMg/MDAxNjAwMjU0OTg4MDA3.gZALdxCG5Z9bp530aIGEljUNoEp0Sc2E-JaXbD8w8bIg.4NH1iDTE9UrX6QjMTpKFKQ-jidu9yjFpPg-gOZ1Btp8g.JPEG.til_t/P20200916_201057123_CC41564F-B33F-441C-A095-3238ADF382B0.jpg)

![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjg0/MDAxNjAwMjU0OTg4NDI0.47l7-gIN4cs_lw082XpM4ITcAUp5-ilD-cnrUDIJaWYg.22VopccAUIv9qFCpjU2k9uPphG4NzK9W4BJxY4u6pXIg.JPEG.til_t/P20200916_201101055_C25E0D84-A346-47B8-8974-3C467F82CBFE.jpg)







택트(tact) 스위치 -> 누르고 있는 동안만 연결이 되는 스위치



원래 a - a'와 b - b'는 연결이 되어 있다

버튼을 누르면 a와 b가 연결이 된다



버튼은 10k 저항





![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTEz/MDAxNjAwMjU1NTI2NTE2.EDUdBnxDt3Kd24O4eAhDokIX3B4Mcb_7bNalzrnCLL4g.ubzkJOA76r4WKw-dVP3IxF5fxgFCudfv_fv1yb1sza4g.PNG.til_t/dsf.png)





저항 반드시 필요, 없다면 5V에 많은 전기가 흐르기 때문

전기는 저항이 없는 쪽으로 흐른다

스위치 누르면 디지털 핀이 LOW

스위치 안 누르면 디지털 핀이 HIGH (디폴트)

이런 스위치를 PULLUP 저항 혹은 PULLUP 스위치라고 부름 

평소에는 스위치는 OFF -> 이때 디지터 입력의 상태는 HIGH이다

**저항이 위에 있다 -> PULLUP**



![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjM1/MDAxNjAwMjU1ODkxOTA4.MxqIFQsTOEjRzPTPjMYe11x0GqWju4ZQ53FNdqyO4Psg.Feh9EjSZOkP3bxey4uvlP0B_sQ2Zz8jruc8DUj9hH9og.PNG.til_t/22222.png)



**이번엔 저항이 밑에 있다 ->PULLDOWN**

평상시에는 디지털 입출력 핀이 LOW (디폴트)

버튼이 눌렸을 경우 전기는 저항이 없는 곳으로 흐르니 HIGH가 된다 



**사람 생각으로는 평소에 LOW, 버튼 눌렸을 때 HIGH가 이해하기 쉬우나** 

**하드웨어에선 PULLUP 방식이 좋다**

**PULLDOWN -> 저항이 위에 연결이 안 되어 전기량이 굉장히 크기 때문에 장시간 연결시 핀에 손상이 갈 수 있다**

**저항이 회로를 보호하고 있기 때문에**



디지털 입력 읽기

digitalRead(핀번호)

\- 해당 핀 번호의 값 읽기

\- HIGH/LOW 리턴



< button_ex01.ino > -> PULLDOWN 버튼 (디폴트 LOW, 누른 경우 HIGH)



![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfOTAg/MDAxNjAwMjU2Nzg5OTEw.nlqws_5Ul7Xzk_cEW6cSsmimN4Uppr5FwzYH5ocDP80g.6xc0AwYk7zw2WFHBKpWzQ8x9hbDerSfmIf6XSVUJdwog.JPEG.til_t/P20200916_204607062_7659E331-7CAF-4D0F-8D2E-661F29A0C1B4.jpg) 



**버튼을 가운데를 연결하는 곳에 꼽는다**

**왼쪽을 10K 저항과 연결하고 나머지 부분을 빵판의 -와 연결한다**

**왼쪽의 위쪽이나 아랫쪽에 점퍼선으로 digital의 11번과 연결한다**

**버튼의 오른쪽 부분을 점퍼선으로 빵판의 +와 연결한다**

**빵판의 +는 power의 5V, 빵판의 -는 power의 GND와 연결한다**

 

int LED = 13;

int BUTTON = 11;

void setup() {

  pinMode(BUTTON, INPUT);

  pinMode(LED, OUTPUT);

}

// 풀다운 (평상시엔 LOW)

void loop() {

  if (digitalRead(BUTTON)) { // 누른 경우 (HIGH)

​    digitalWrite(LED, HIGH);

  } else {

​    digitalWrite(LED, LOW);

  }

  delay(10);

}





< button_ex02.ino > -> PULLUP 버튼 (디폴트 HIGH, 누른 경우 LOW)



![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTkx/MDAxNjAwMjU3MDIyNTUw.TDwysr6olVemLkRpIpXJy3BZEJ7FBttS_f-6O5dS08Eg.DOoSYrHXvD_VLAhaEACsAF03CQ9nB7G6oDvGY5aLkW4g.JPEG.til_t/P20200916_205003813_BF1F8F82-8F8B-4D25-B50C-21884CF3FAB0.jpg) 



**버튼을 가운데를 연결하는 곳에 꼽는다**

**아까와 반대로 왼쪽을 10K 저항과 연결하고 나머지 부분을 빵판의 +와 연결한다**

**왼쪽의 위쪽이나 아랫쪽에 점퍼선으로 digital의 11번과 연결한다**

**버튼의 오른쪽 부분을 점퍼선으로 빵판의 -와 연결한다**

**빵판의 +는 power의 5V, 빵판의 -는 power의 GND와 연결한다**



int LED = 13;

int BUTTON = 11;

void setup() {

  pinMode(BUTTON, INPUT);

  pinMode(LED, OUTPUT);

}

// 풀업 (평상시엔 HIGH)

void loop() {

  if (digitalRead(BUTTON) == LOW) { // 누른 경우 LOW

​    digitalWrite(LED, HIGH);

  } else {

​    digitalWrite(LED, LOW);

  }

  delay(10);

}



﻿아두이노가 지원해주는 내부 PULLUP 

그냥 PULLUP은 저항도 꼽고 번거롭다 

아두이노 내부의 저항을 이용하자!



**내부 PULLUP 방식**

![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMjM5/MDAxNjAwMjU3NDAwNDQw.nRWsQCT9jYAfMVg_Ve51D_GjyC8YTL1aAtwPokBlE0Ag.1U7IbXaDltCOqRxLfBMS8j6CrJFqeihDYMEA3JA1P-Ig.PNG.til_t/3333.png)



< button_ex03.ino > -> 내부 PULLUP 사용





![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfNjEg/MDAxNjAwMjU3NTg4NTkx.vr2OpssCaM3NJ-ZTJSFYxVlyhJMx0tIjr3BZt9WOqgog.UGqylfYdS1i4rwKuZ4j4_FCIkQ9jxxR4Ap_69VufBGcg.JPEG.til_t/P20200916_205901808_F6716D9E-5F0C-46BB-97BB-F48AD53FCB21.jpg) 





**PULLUP 상태에서 저항만 제거한다**





const int ledPin = 13;

const int inputPin = 11;

void setup() {

  pinMode(ledPin, OUTPUT);

  pinMode(inputPin, INPUT_PULLUP); // 내부 풀업 스위치

}

void loop() {

  int swInput = digitalRead(inputPin);

  if (swInput == LOW) // 스위치를 누르면

​    digitalWrite(ledPin, HIGH);

  else

​    digitalWrite(ledPin, LOW);

}





﻿ 

< button_ex04.ino > -> 4번 led는 1초 간격으로 블링크, 3번 led는 버튼을 누르면 켜진다





![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfNTIg/MDAxNjAwMjU4MTg3OTUz.0OBhWJohca5m0RxF3CCaT2h0BOe01QooiTfodqlicwog.SBs6lwFKbv6Om0vxVBibZyuoDkp-ftlC_bJeK0N_tEog.JPEG.til_t/IMG_0933.jpg)





**버튼은 그대로 두고 3번과 4번에 led의 +를 연결해준다**

**led의 - 부분에는 저항을 연결하고 나머지 저항의 다리에는 빵판의 -를 연결한다**







\#include <SimpleTimer.h>



SimpleTimer timer;

int pin_LED1 = 4;

int pin_LED2 = 3;

int pin_button = 11;

boolean LED_state = false;



// 모든 C++의 함수명의 의미 -> 함수 시작주소를 가지고 있는 포인터 상수



void blink() {

  LED_state = !LED_state;

  digitalWrite(pin_LED1, LED_state);

}



void setup() {

  pinMode(pin_LED1, OUTPUT);

  digitalWrite(pin_LED1, LED_state);

  pinMode(pin_LED2, OUTPUT);

  digitalWrite(pin_LED2, false);



  pinMode(pin_button, INPUT_PULLUP);

  timer.setInterval(1000, blink); // 함수의 주소 넘긴 것, 함수를 매개변수로 전달 (blink)



}



void loop() {

  timer.run(); // 타이머 운영

  // 버튼 상태를 읽어서 13번 핀에 연결된 LED에 표시

  digitalWrite(pin_LED2, !digitalRead(pin_button));

}







< button_ex06.ino > -> 디지털 신호 입력 시간 측정하기





const int pin_button = 11;

long startTime = 0;

long swCountTimer = 0;



void setup() {

  Serial.begin(9600);

  pinMode(pin_button, INPUT_PULLUP);

}

void loop() {

  if (digitalRead(pin_button) == LOW) { // 스위치가 눌러진 경우

​    startTime = millis(); // 현재 시간 측정

​    while (digitalRead(pin_button) == LOW); // 눌러진 시간 동안 지연, {};와 같다

​    // 버튼을 눌러서 뗄 때까지 while문을 돈다 



​    // 스위치를 뗀 시간을 측정하여 차이 계산

​    swCountTimer = millis() - startTime; 

​    // swCountTimer는 스위치를 눌렀던 시간

​    

​    Serial.print(swCountTimer);

​    Serial.println(" ms");

  }

}







![img](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTc3/MDAxNjAwMjU5MzU0ODEz.4Z3cuQCNXi486VVelRhm5xu4HccftblTsC_mP_8EBnEg.qtl3cTdsi9Dgzu73EtD7nRSE9mBLJUjkqg7jroJ8z30g.PNG.til_t/%ED%9E%98%EB%93%9C%EB%84%A4.png) 





**채터링 -> 버튼을 누르거나 뗄 때 물리적으로 접촉 발생으로 짧은 시간 동안 On/Off를 반복하는 것**



평상시에 HIGH, 누를 때 LOW

**우리는 한 번 누른 것 같지만 실제론 접촉면이 짧은 시간에 붙었다 떨어졌다를 반복한다 (여러번 폴링과 라이징) -> 바운스**



**해결 방법(디바운스, debounce) -> 채터링이 끝날 때까지 조금 대기**





**스위치를 한 번 눌렀을 땐 켜지고 또 한 번 누르면 꺼지게 하고 싶다 (계속 누를 필요 없게)**



지금까지는 digitalRead로 현재 값이 HIGH or LOW를 측정했다

**그런데 의도대로 스위치를 온오프하려면 떨어지는 시점을 알아야 한다**



**두 번 측정 -> 첫 번째 읽었을 때와 두 번째 읽었을 때의 상태를 비교한다**



첫 번째 상태 (OFF), 두 번째 상태(OFF)

첫 번째 상태 (OFF), 두 번째 상태(ON) -> Falling Edge (누를 때)

첫 번째 상태 (ON), 두 번째 상태(ON)

첫 번째 상태 (ON), 두 번째 상태(OFF) -> Rising Edge (뗄 때)





<button_ex07.ino > -> 버튼 누른 횟수 세기







int pin_button = 11;

boolean state_previous = true; // 풀업이기 때문에

boolean state_current;

int count = 0;

void setup() {

  Serial.begin(9600);

  pinMode(pin_button, INPUT_PULLUP);

}

void loop() {

  state_current = digitalRead(pin_button); // 상태 읽어 state_current에 저장

  if (!state_current) { // 누른 경우

​    if (state_previous == true) { // 이전상태가 true였다면(current:L, previous:H) -> falling edge

​      count++;

​      state_previous = false;

​      Serial.println(count);

​    }

​    delay(10); // 추가

  } else {

​    state_previous = true;

  }

}







**led1은 누르면 불이 켜지게, led2는 한 번 누르면 켜지고 다시 누르면 꺼지게, led3은 누르면 블링크 다시 누르면 블링크 꺼지게**

**
**

**
**

**![IMG_0940.jpg](https://blogfiles.pstatic.net/MjAyMDA5MTZfODQg/MDAxNjAwMjYyNTQ5MDMx.BOrtwq7hy5gpcmX8KL-tGyVmVlED5ETQK8oaW3Leig4g.HNMDwe-DPlbozyeC76q2MXzsrE1fBNWLTArYNO6Wq-Ag.JPEG.til_t/IMG_0940.jpg)

![IMG_0941.jpg](https://blogfiles.pstatic.net/MjAyMDA5MTZfMTEg/MDAxNjAwMjYyNTQ5NDY2._3TpfEahx-Zp7brBv6a-mdBvvdas6ci0D5mYqui0QBkg.td8uCgO4EetJ_vn2klXhtaW3ex_W3azK6crlSPUlR2gg.JPEG.til_t/IMG_0941.jpg)
**

**
**

**
**

**저번에 만들었던 신호등과 버튼 세 개가 부착된 미니 브레드보드를 연결한다**

**신호등의 -를 점퍼선으로 연결해서 버튼의 한 쪽을 연결해 마지막 빵판의 -까지 연결한 후 다른 점퍼선으로 빵판의 -와 아두이노의 power의 GND를 연결한다**

**나머지 스위치의 _는 각각 디지털 핀에 연결한다**

**마찬가지로 led의 +들도 각각의 디지털 핀에 연결한다**

**
**



소스를 객체지향으로 바꾸자



< Led.h >





\#pragma once

\#include <Arduino.h>





class Led{

  protected:

​    int pin;

  public:

​    Led(int pin);

​    void on();

​    void off();

​    void toggle();

​    void set(int value); // 변수로 값을 관리해서 그 값으로 출력해라

};







< Led.cpp >







\#include "Led.h"



Led::Led(int pin) : pin(pin){

  pinMode(pin, OUTPUT);



}

void Led::on(){

  digitalWrite(pin, HIGH);

}

void Led::off(){

  digitalWrite(pin, LOW);

}

void Led::toggle(){

  int state = digitalRead(pin);

  digitalWrite(pin, !state);

}

void Led::set(int value){

  digitalWrite(pin, value);

}







< Button.h >





\#pragma once

\#include <Arduino.h>



class Button{

  protected:

​    int pin;

​    bool state_previous;

​    bool state_current;

​    void (*callback)();

  public:

​    Button(int pin);

​    int read();

​    void setCallback(void (*callback)());

​    int check();

};







< Button.cpp >





\#include "Button.h"





Button::Button(int pin) : pin(pin){

  pinMode(pin, INPUT_PULLUP);

  state_previous = true;

  callback = NULL;

}



int Button::read(){

  return !digitalRead(pin); 

  // 실제 하드웨어는 풀업이지만, 소프트웨어에서는 풀다운인 것처럼 연계할 것(반전시킴)

}



void Button::setCallback(void (*callback)()) {

  this->callback = callback;

}



int Button::check(){

  state_current = digitalRead(pin);

  if(!state_current) { // 누른 경우

if(state_previous == true) {

  state_previous = false;

  //버튼을 누른 시점에서 해야 할 작업

  // work();

  if(callback != NULL){

  callback();

}

}

delay(5);

} else {

state_previous = true;

}

}







< button_ex07.ino >





\#include "Led.h"



\#include <SimpleTimer.h>



SimpleTimer timer;

// int pin_button = 11;

// int led = 4;

Led led1(3);

Led led2(4);

Led led3(5);

Button btn1(9);

Button btn2(10);

Button btn3(11);



bool blinkPlay = false; // 블링크 중인지 여부, 디폴트는 중지

int blinkTimer = -1; // 블링크용 타이머 id



// boolean state_previous = true;

// boolean state_current;

// int count = 0;

void led2OnOff() {

  led2.toggle();

}



void led3Blink() {

  led3.toggle();

}



void led3BlinkControl() {

  blinkPlay = !blinkPlay; // 상태반전

  if (!blinkPlay) { // 이제 블링크 중지면

​    led3.off();

  }

  timer.toggle(blinkTimer); // 타이머 활성/비활성 토글

}

void setup() {

  Serial.begin(9600);

  // pinMode(pin_button, INPUT_PULLUP);

  // pinMode(led, OUTPUT);

  btn2.setCallback(led2OnOff);

  btn3.setCallback(led3BlinkControl);

  blinkTimer = timer.setInterval(500, led3Blink);

  timer.disable(blinkTimer); // 타이머 중지 상태로 시작

}



void work() {

  led1.toggle();

  // int ledState = digitalRead(led);

  // digitalWrite(led, !ledState);

  // count++;

  // Serial.println(count);

}





void loop() {

  // led.set(btn.read()); // 풀업버튼인 경우 반전

  timer.run();

  led1.set(btn1.read());

  btn2.check();

  btn3.check(); // 에지(falling)이 발생했는지 체크

  // state_current = digitalRead(pin_button);

  // led.set(!state_current);

  // if(!state_current) { // 누른 경우

  // if(state_previous == true) {

  //   state_previous = false;

  //   //버튼을 누른 시점에서 해야 할 작업

  //   work();



  // }

  // delay(5);

  // } else {

  // state_previous = true;

  // }

}









**버튼과 led, lcd로 동작하는 스탑워치 만들기**

(맨 왼쪽의 버튼 -> start and stop

중간 버튼 -> lap time

오른쪽 버튼 -> reset

led1 -> 시간 재는 동안 blink

led2 -> 리셋시 불 켜짐)





< stopwatch.ino >





\#include <Led.h>



\#include <Button.h>



\#include <SimpleTimer.h>



\#include <LiquidCrystal_I2C.h>



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

​    // 최초 기동 시작

​    startTime = millis(); // 기준 시간 설정

​    timer.enable(blinkTimerId);

​    led2.off();

​    state = true; // 기동중임을 설정

  }

  timer.toggle(timerId);



}



void laptime() {

  if (state) { // 가동중일 때만 출력

​    unsigned long t = millis();

​    unsigned long diff = t - startTime;

​    printTime(diff, 1);

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





![동영상은 수정하실 수 없습니다.](https://ssl.pstatic.net/static.se2/static/img/alter_video.png)