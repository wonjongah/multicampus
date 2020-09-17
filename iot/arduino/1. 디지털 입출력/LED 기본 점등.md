

#### < LED 기본 점등 >



![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjcw/MDAxNTk5NzA4NjExMTk1.2DbMOGGX_U3OmVO5qyFMnkWFLL6GTpJNjVDS397Zz3kg.e6iudxlfTXsRBV0aHddpB55alE7VX8APcNtSgW5Supcg.PNG.til_t/%EC%BA%A1%EC%B2%98.PNG?type=w1) 







﻿setup() -> 초기화할 때 딱 한 번 실행, 리셋되면 다시 setup 

보내는 쪽과 받는 쪽의 속도가 같아야 한다, 보드레이트와 Serial.begin(속도)





![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjk4/MDAxNTk5NzA4NzMwMTQ3.YV-CFbjGfiXDZzES7XqQKzPaIyUGNFFZNAk_qdOmIZAg.AVne4KW8mG4l-XCXo_cNboG6rmG2VK-7KknR61swHIQg.JPEG.til_t/P20200910_104246804_D454163A-5CD8-4EC9-B48F-303C5B6C8081.jpg?type=w1)



﻿직류 사용할 것



아두이노의 POWER 라벨을 보면 

Vin -> 외부 전원을 사용할 때, 컴퓨터와 연결하지 않을 때(건전지) 사용

5V -> +와 연결

GND -> -극, 빵판의 GND와 연결을 해야 함

3.3V -> 3.3V로 동작하는 것들은 3.3V로 연결







![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfNTUg/MDAxNTk5NzA4NzMyMzE4.t6D2pJklvy6INNTFnCfv_4zfh_T-2nfOtSIhUyVEWjog.imiFCIrXlLoXjphWGH0KRpHi09WRbAkiMLPDKfLudIwg.JPEG.til_t/P20200910_104248877_84E7ADC4-0659-46D7-949A-7CE5F03FF4FC.jpg?type=w1)



브레드보드(빵판)

빨강 (+) (VCC) -> 전원을 들어오게 하겠다

파랑 (-) (GND)

+와 - 부분은 가로로 연결되어 있다



가운데는 세로로 연결되어 있다(abcd... 이런식으로 알파벳 써있는 곳)

위 파트와 아래 파트로 분리되어 있다

물리적으로 분리된 부분은 실제로도 떨어져 있어서 연결을 해줘야 함



점퍼선

빨강(VCC), 검정(GND)

긴 것(전원), 짧은 것(부품 연결)

+와 -를 바로 연결하면 안 된다

배선작업을 할 땐 usb 빼고 작업






![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMTky/MDAxNTk5NzA4NzMwNTA1.YQK4sRK-Ygh2duUiQbphNdbIv-cl7aSs-aNDWtpdb7og.ZaFBB3o_h1UhlcIEJrrdR5w4k5N2E2qi8tcGbkCdAWAg.JPEG.til_t/P20200910_104442265_BDE98F84-F36A-42F3-875D-6BFA6409F9F1.jpg?type=w1)


 

+에서 -로 흐르게 하는 것이 다이오드이다

거기에 빛까지 내게 하는 것이 발광 다이오드

다리의 길이로 +, -를 구분한다

긴 쪽이 +극(anode), 짧은 쪽이 -극(cathode)





![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjcy/MDAxNTk5NzA4NzMwODc5.9p_vyp96kqRgNxMEhfq4bB1Xy1sEUKmAer-B_xIvbQwg.f6CxFR1-fWAVrqm--XFPDy8lkMCwVhyvXYJ5siH2Kn4g.JPEG.til_t/P20200910_104859482_E206563B-8F34-4AD6-8A20-B8411333AECE.jpg?type=w1)

![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjQ1/MDAxNTk5NzA4NzMxNTQ2.-1HSbmbXQRp-1_VM_PLqsl_9kXkL2QUPCdKAidSANakg.sfI63IDbA8bPwuy5ydfdl9W_IhpV0RBHBiW1EgcKO04g.JPEG.til_t/P20200910_105000791_311DCED3-BFF2-40E2-ACDB-484812335E7B.jpg?type=w1)
 





﻿다리가 꺾인 쪽이 + 







![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMTQg/MDAxNTk5NzA4NzMyMDA4.TrfXfKBMUtEKtObthTjN2rvN7jIiCtLNSiwkEA_aPSgg.10TzU32mzo0LEhjVf7ZHbgld0PvvuRautDf8uOdB4wYg.JPEG.til_t/P20200910_110923892_1ABEC2FF-305E-4472-8E74-555DFC496EAB.jpg?type=w1)



﻿저항(R)(Resist) -> 전기의 흐름 제한

led에 연결할 것은 330

색마다 색이 지정되어 있다 (첫째 숫자, 둘째 숫자, 0의 개수, 저항값의 오차)




![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfNTUg/MDAxNTk5NzA4NzMyMzE4.t6D2pJklvy6INNTFnCfv_4zfh_T-2nfOtSIhUyVEWjog.imiFCIrXlLoXjphWGH0KRpHi09WRbAkiMLPDKfLudIwg.JPEG.til_t/P20200910_104248877_84E7ADC4-0659-46D7-949A-7CE5F03FF4FC.jpg?type=w1)



 

**빨간 선을 아두이노의 5V와 연결한다, 반대쪽 남은 선을 빵판의 +에 연결한다**

**검정 선을 아두이노의 GND에 연결한다, 반대쪽 남은 선을 빵판의 -에 연결한다**

**
**

**
**

![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjYx/MDAxNTk5NzA4NzMyNjg3.dmRG6sLeIuuyi2ccunhTJGFBzlnkUgUEU2L6UFNR_qgg.S2x_8tgGn8PoqKT2i31x3R0PjUeRgQoS3a7TcYZjSKkg.JPEG.til_t/P20200910_111449297_9A61C31C-BA2E-4239-A2B7-78B714DFF01A.jpg?type=w1)


**
저항이 -와 세로로 아랫쪽에 연결되도록 꼽는다**

**led는 +와 -를 구분하므로, 저항이 -를 연결하고 있기 때문에 led의 짧은 다리(-)을 연결해야 한다**

**점퍼선으로 +와 led의 +를 연결한다**

**아두이노의 UBS 연결하면 불이 들어온다**

**-> 아두이노의 +로 전기가 들어와서 불 들어오게 하고 저항으로 와서 소진한다**

같은 라인에는 두 개의 다리를 같이 꼽으면 안 된다 (연결해주는 다리라고 생각하기)






![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjgz/MDAxNTk5NzA4NzMzMTE0.zsL8HvyJGyYsudTFf1PFyTSH5d4FGp01NmPbVSFZerwg.UVy64yv7QXMHIuUQlg7W69lu-EnXo0Sh9y45RB1rCHUg.JPEG.til_t/P20200910_111709029_DAA6ED56-0871-4861-86AB-F251572A3F9A.jpg?type=w1)



﻿**소프트웨어적으로 led를 켰다가 끌 것**

**초록색 점퍼선을 아두이노의 13번에 꼽고 led의 +와 연결**

**
**

﻿pinMode(핀번호, 모드) 

\- 핀번호 : 모드를 설정하고자 하는 핀 번호

\- 모드 : 출력일 경우 OUTPUT, 입력일 경우 INPUT



﻿digitalWrite(핀번호, 전압) 

\- digitalWrite를 사용하려는 핀은 꼭 pinMode를 출력모드로 설정해야 한다

\- 핀번호 : 전압을 설정하고자 하는 핀번호

\- 전압 : HIGH인 경우 HIGH를 입력하고, LOW인 경우 LOW 입력한다

(high, 1, true) -> 전기를 내보내겠다

(low, 0, false) -> 끌 것

ex) digitalWrtie(13, HIGH); -> 13번 선으로 +를 내보내겠다



delay(멈출 시간)



**< ex01.ino >**





void setup() {

 pinMode(13, OUTPUT);

 digitalWrite(13, false); // led 끄겠다

}



void loop() {

 digitalWrite(13, HIGH); // 13번에 high

 delay(1000); // 1초 동안 high 계속 나가고 있음, 바꾸지 않는 이상 계속 나감

 digitalWrite(13, LOW); // 끄겠다

 delay(1000); // 끄는 걸 1초동안 계속

}









![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjcg/MDAxNTk5NzA4NzMzNDg2.nY--ZQ9aI8HD55wRIWKyxLZPsQCW_ZcxN7AZG6HAjQIg.r1EUgcC70cLAOKJ-zKpVtIiUKM_UAtulQy0-wZQMuK4g.JPEG.til_t/P20200910_113640598_4BA07A17-FEB4-4A9D-ABC1-EDB9C46BDC74.jpg?type=w1) 





전기가 흐르기 위해서 전압이 달라야 한다 (높은 전압에서 낮은 전압으로 흐름)

13번 핀에 0을 주냐 혹은 1을 주냐에 따라서 전위차가 달라진다

digitalWrite(13, false); -> led 끄겠다



 

**< ex02.ino >**





int pin_LED = 13; // 핀 번호를 전역변수로 관리





boolean LED_state = false; // LED의 상태를 전역변수로 관리





void setup() {



 pinMode(pin_LED, OUTPUT);



 digitalWrite(pin_LED, LED_state);



}





void loop() {



 LED_state = !LED_state; // 반전, toggle (켜있으면 끄게, 꺼져있으면 켜지게)



 digitalWrite(pin_LED, LED_state);



 delay(1000);



} // built in led

**
**

**
**

**< ex03.ino >**

**
**

int pin_LED = 7;





void blink(int pin, long time){



 digitalWrite(pin, HIGH);



 delay(time);



 digitalWrite(pin, LOW);



 delay(time);



}



void setup() {



 pinMode(pin_LED, OUTPUT);



}





void loop() {



 blink(pin_LED, 500);



 blink(pin_LED, 1000);



 blink(pin_LED, 2000);



 



}







![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfNDIg/MDAxNTk5NzIzNTgwODg1.zZsu32_icySRMgx8Q-jC5Q29mq6RRz0KFd0XzQkB4DMg.MURfuDGhOuRakC-krB8ytCaXVF0aYdYdnTYp2b_P2V4g.JPEG.til_t/P20200910_132549374_721F9869-C3BF-445C-9BFE-A8E7F210EAC7.jpg?type=w1) 





﻿led 하나 더 추가하기

번갈아 가면서 깜빡이는 예제



**< ex04.ino >**



const int pin_LED1 = 7;



const int pin_LED2 = 6;



void setup() {



  pinMode(pin_LED1, OUTPUT);



  pinMode(pin_LED2, OUTPUT);



}





void loop() {



 digitalWrite(pin_LED1, HIGH);



 digitalWrite(pin_LED2, LOW);



 delay(100);





 digitalWrite(pin_LED1, LOW);



 digitalWrite(pin_LED2, HIGH);



 delay(100);



}

**
**

**< ex05.ino >**



int pin_LED1 = 7;



int pin_LED2 = 6;



void setup() {



 pinMode(pin_LED1, OUTPUT);



 pinMode(pin_LED2, OUTPUT);





 digitalWrite(pin_LED1, LOW);



 digitalWrite(pin_LED2, LOW);



}





void loop() {



 digitalWrite(pin_LED1, HIGH);



 delay(500);





 digitalWrite(pin_LED1, LOW);



 digitalWrite(pin_LED2, HIGH);



 delay(500);



 



 digitalWrite(pin_LED1, HIGH);



 delay(500);





 digitalWrite(pin_LED1, LOW);



 digitalWrite(pin_LED2, LOW);



 delay(500);





}



**
**

**
**

**![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfODUg/MDAxNTk5NzI0MjY0NjY3.1epU06mDYox-u3H3RtlpbzrYvBblYEizsIwScVNjxacg.cSLZ-SqpFDUneP-qJJiZLsErs5JfsRFf3pJWf4HwbAUg.JPEG.til_t/P20200910_142847146_DC8D0129-6022-4082-90FF-BD5689DEF5E3.jpg?type=w1)**

**
**



같은 방법으로 led 하나 더 설치



**< ex06.ino>**



int pin_LED1 = 7;



int pin_LED2 = 6;



int pin_LED3 = 5;



void setup()



{



 pinMode(pin_LED1, OUTPUT);



 pinMode(pin_LED2, OUTPUT);



 pinMode(pin_LED3, OUTPUT);



}



void loop()



{



 digitalWrite(pin_LED1, HIGH);



 delay(2000);



 digitalWrite(pin_LED1, LOW);



 digitalWrite(pin_LED2, HIGH);



 delay(1000);



 digitalWrite(pin_LED2, LOW);



 digitalWrite(pin_LED3, HIGH);



 delay(2000);



 digitalWrite(pin_LED3, LOW);



}





**< ex07.ino >**



int redLED = 7;



int yellowLED = 6;



int greenLED = 5;



void setup()



{



 pinMode(redLED, OUTPUT);



 pinMode(yellowLED, OUTPUT);



 pinMode(greenLED, OUTPUT);



}



void go(int duration = 0){



 digitalWrite(redLED, LOW);



 digitalWrite(yellowLED, LOW);



 digitalWrite(greenLED, HIGH);



 if(duration!=0){



  delay(duration);



 }



}



void stop(int duration = 0){



 digitalWrite(redLED, HIGH);



 digitalWrite(yellowLED, LOW);



 digitalWrite(greenLED, LOW);



 if(duration!=0){



  delay(duration);



 }



}



void leftTurn(int duration = 0){



 digitalWrite(redLED, LOW);



 digitalWrite(yellowLED, HIGH);



 digitalWrite(greenLED, HIGH);



 if(duration!=0){



  delay(duration);



 }



}



// 2초간 직진 신호



// 1초간 직진, 좌회전 신호



// 2초간 정지 신호



void loop()



{



 go(2000);



 leftTurn(1000);



 stop(2000);



}

**
**

그러나 ex07은 코드 중복이 너무 많다

이걸 헤더파일과 cpp파일로 나누어서 관리할 것



**< ex07_led/app.ino >**



\#include <TrafficLight.h>



TrafficLight lights(7, 6, 5); // 전역변수로 만들고 핀의 번호 넘겨준다



void setup()

{

  

}





// 2초간 직진 신호

// 1초간 직진, 좌회전 신호

// 2초간 직진 및 좌회전 블링크

// 2초간 정지 신호

void loop()

{

  lights.run();

}



**< Arduino/libraries/mylib/TrafficLight.h >**



\#ifndef __TRAFFIC_LIGHT_H__

\#define __TRAFFIC_LIGHT_H__

// include 한 번만 해라



\#include <Arduino.h>



class TrafficLight{

private: // 멤버 변수의 접근 제어자

  int redLED;

  int yellowLED;

  int greenLED;



public: // 멤버 함수의 접근 제어자

  TrafficLight(int redLED, int yellowLED, int greenLED); // 함수의 원형

  

  void go(int duration = 0);

  void leftTurn(int duration = 0);

  void leftTurnWarning(int duration = 0);

  void stop(int duration = 0);

  void blink(int pin, int duration);



  void run(); // 신호등 운영 메서드

};



\#endif



**< Arduino/libraries/mylib/TrafficLight.cpp >**





\#include "TrafficLight.h"



  TrafficLight::TrafficLight(int redLED, int yellowLED, int greenLED)

  : greenLED(greenLED), yellowLED(yellowLED), redLED(redLED) // 멤버 초기화 리스트 형식으로 초기화

  // this->greenLED = greenLED;

  {

​    pinMode(redLED, OUTPUT);

​    pinMode(yellowLED, OUTPUT);

​    pinMode(greenLED, OUTPUT);

  }

  void TrafficLight::go(int duration){ // 디폴트 값은 헤더에만 있으면 된다

​    digitalWrite(redLED, LOW);

​    digitalWrite(yellowLED, LOW);

​    digitalWrite(greenLED, HIGH);

​    if(duration!=0){

​      delay(duration);

​    }

  }

  void TrafficLight::leftTurn(int duration){

​    digitalWrite(redLED, LOW);

​    digitalWrite(yellowLED, HIGH);

​    digitalWrite(greenLED, HIGH);

​    if(duration!=0){

​      delay(duration);

​    }

  }

  void TrafficLight::leftTurnWarning(int duration){

​    digitalWrite(redLED, LOW);

​    digitalWrite(greenLED, HIGH);

​    // 5회 점등

​    int interval = duration / 5;

​    for (int i =0; i < 5; i++){

​      blink(yellowLED, interval);

​    }

  }

  void TrafficLight::stop(int duration){

​    digitalWrite(redLED, HIGH);

​    digitalWrite(yellowLED, LOW);

​    digitalWrite(greenLED, LOW);

​    if(duration!=0){

​      delay(duration);

​    }

  }

  void TrafficLight::blink(int pin, int duration){

​    digitalWrite(pin, HIGH);

​    delay(duration/2);

​    digitalWrite(pin, LOW);

​    delay(duration/2);

  }



  void TrafficLight::run(){

​    go(2000);

​    leftTurn(1000);

​    leftTurnWarning(2000);

​    stop(2000);

  } 

![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAYAAAA7KqwyAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3wccBTIrwFRftwAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAD0lEQVQoz2NgGAWjgAoAAAJJAAEMrHXpAAAAAElFTkSuQmCC)





![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMzUg/MDAxNTk5NzI2MzYzMjIz.sHOcuxgkmQK2dIVbApmKSjtf2STEIHmjetYAbCuNhvog.YbfN_PljUSySrwT98UtkwDOQ5iEAjhZTCO6VAobDMTYg.JPEG.til_t/P20200910_170944471_237CA8E1-20B8-48FB-84BC-543C5AE536AD.jpg?type=w1)



하드웨어의 모듈화



![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMTEz/MDAxNTk5NzI2NTAxMzAy.YuOgMRgFksa5iU0qcdi2DmGXwtFWnPzPS6ucJCNBJuIg.yVKjZdKSmcP5XdAIK80630Kbmol6JbTyAqNipaO19-Ag.JPEG.til_t/P20200910_171529699_ECE99F17-3FE9-4A03-BEFC-069941864802.jpg?type=w1)



미니 브레드 보드

왼쪽의 세로가 GND를 의미한다

아까와 동일하게 led를 연결하고 저항을 왼쪽과 led를 맞춰서 연결한다


![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjAw/MDAxNTk5NzI2MzY0MDUz.8OKyNYiDLQ0m0RvtoIlAKzrSNDMkt94j0Rf1arp7j2gg.rJqFkIfVKSA4yc4NqlOpy0McZqnBHJz4WqDPpnqDtIIg.JPEG.til_t/P20200910_172505891_F5954485-68FF-46A2-9D0C-4A47BF8FFBCF.jpg?type=w1)



GND 쪽에 우노에 연결했던 GND를 연결해주고, 각 핀에 꼽았던 점퍼선을 색에 맞추어 연결한다

+는 핀에서 나오니 이번엔 굳이 빵판에 꼽지 않는다


![img](https://blogfiles.pstatic.net/MjAyMDA5MTBfMjQ0/MDAxNTk5NzI2MzY0MzQ3.TLrNg4CD6HGz4qxlsagpky07fMsgE-5k8fnQpPNSunEg.Xq_CQAegd-6AuflZld7dXLtdCiOzgokSGWbF3tRDFIAg.JPEG.til_t/P20200910_172501445_1F6BC828-AD38-4FFD-B65A-242079F038EC.jpg?type=w1) 



이렇게 미니 브레드보드를 이용하면 하드웨어 또한 모듈화할 수 있다