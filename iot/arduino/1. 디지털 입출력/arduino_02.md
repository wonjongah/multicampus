![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfNjAg/MDAxNTk5Nzg1MDA0OTI0.6gqlZreYCVF976ckj1rIBJ6qV1FU1kQ2NsABGCzvtdYg.QVqecd7OozB6c8VwUltLV5mKISEDyVdJzEr3xowBhTcg.JPEG.til_t/P20200911_092314756_4FDE432E-6B03-4960-9B55-8EB948C9C7C0.jpg)





**led 네 개를 순서대로 연결하고 그에 따라 저항도 led의 -에 맞춰서 연결한다**



![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjE1/MDAxNTk5Nzg1MDA1NjQw.W8RWMVAFpHhyKDfNv-_yCiijmmtbA58EvgIxMzI_2cAg.5D7fm5Wz5Ekcs25nTKKeHPi0CaCkmeLFT87WTwsret0g.JPEG.til_t/P20200911_092459474_D973322C-E34B-405B-A883-F85438FA1CE0.jpg)







**핀 번호(+)와 led의 +를 연결한다**





![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfOTEg/MDAxNTk5Nzg1MDA1ODc5.p-W2e-59k5Z4pKcm9HqsTffcER5gVW_W54KQc7s_JaMg.dNbk7KyhM_4_5otgTS0-dHqsEnRYNMTeKkYcqiVOrUog.JPEG.til_t/P20200911_093445152_9F0135C7-FDF5-4E8C-AE3C-7906E1F4ECAE.jpg) 





**아두이노의 GND와 빵판의 GND를 연결한다** 

**vscode에서 uno인지 체크, 속도가 9600인지 체크, arduino.json에서 지금 컴파일하려는 폴더 바꾸기, 포트와 연결 잘 됐는지 확인(COM4)**





< ex08_led_array.ino > -> 순차적으로 불 들어오는 것을 핀 배열과 반복문을 통해 구현







int pins[] = {3, 5, 7, 9};

int state = 0;



void setup(){

  Serial.begin(9600);

  for(int i = 0; i < 4; i++){

​    pinMode(pins[i], OUTPUT);

​    digitalWrite(pins[i], LOW);

  }

}



void loop(){

  for(int i = 0; i < 4; i++){ // 0 X X X 

​    if(i==state){

​      Serial.print("0 ");

​      digitalWrite(pins[i], HIGH);

​    } else{

​      Serial.print("X ");

​      digitalWrite(pins[i], LOW);

​    }

  }

  Serial.println();

  state = (state + 1) % 4; // 0~3

  delay(1000);

}









< ex09_led_serial.ino > -> 시리얼 입력으로 끄고 켜기







int pin_LED = 13; 

// 특수하게 13번 핀은 보드에 있는 led로 출력 가능



void setup(){

  Serial.begin(9600);

  pinMode(pin_LED, OUTPUT);

}



void loop(){

  if(Serial.available()){ // 수신된 데이터가 있냐, 수신데이터가 있으면 true, 없으면 false

​    char inChar = Serial.read(); // read() 글자 하나를 읽는다

​    if(inChar == '\r' || inChar == '\n'){

​      return;

​    }

​    if(inChar == '1'){ // 문자 1이면 불을 키겠다

​      digitalWrite(pin_LED, HIGH);

​    }

​    else{

​      digitalWrite(pin_LED, LOW);

​    }

  }

}







**F1을 누르고 send text to serial port를 누르고 1을 입력하면 불이 들어온다**





< ex10_led_seiral.ino > -> 입력한 인덱스에 따라서 led 점등







int pins[] = {3, 5, 7, 13};

int state = 0;



void setup(){

  Serial.begin(9600);

  for(int i = 0; i < 4; i++){

​    pinMode(pins[i], LOW);

  }

}



void loop(){

  if(Serial.available()){

​    char data = Serial.read();

​    if(data == '\r' || data == '\n'){

​      return;

​    }

​    Serial.println(String("You entered \'") + data + '\'');



​    if(data >= '1' && data <= '4'){

​    state = data - '0' - 1; // LED 인덱스 변환, 대상이 되는 인덱스 결정

​    // data는 문자 코드 실제 숫자로 90이라고 가정해보자, 난 필요한 게 실제 숫자 1이 필요하다

​    // int()와 같은 과정

​    // '1'(90) - '0'(89) = 1

​    // 0으로 만들기 위해 1을 뺀 것

​    // 입력한 문자열 데이터를 실제 led의 숫자로 바꾸기 위한 연산

​    Serial.print("LED ");

​    Serial.print(state + 1);

​    Serial.println("  i On... ");

​    }else

​    {

​      Serial.println("* Invalid LED number ... ");

​      state = -1;

​    }

​    for(int i = 0; i < 4; i++){

​      if(i == state){

​        Serial.print("0 ");

​        digitalWrite(pins[i], HIGH);

​      }else

​      {

​        Serial.print("X ");

​        digitalWrite(pins[i], LOW);

​      }

​      

​    }

​    Serial.println();

​    }

  

  

}







**F1을 누르고 send text to serial port를 누르고 1, 2, 3, 4을 입력하면 각기 인덱스의 불이 들어온다**

**
**

**
**

< ex11.ino > -> 지정한 핀의 led가 delay를 쓰지 않고 깜빡이게 하기(동시 작업 기초)



**
**

int pin_LED = 13;

boolean LED_state = false;

unsigned long time_p, time_c;

unsigned long count = 0;



void setup(){

  pinMode(pin_LED, OUTPUT);

  digitalWrite(pin_LED, LED_state);

  Serial.begin(9600);

  time_p = millis(); // 현재 시간으로 ms 리턴

}



void loop(){

  time_c = millis();

  count++;



  // 1초 이상 시간이 경과한 경우

  if(time_c - time_p >= 1000){

​    time_p = time_c;



​    LED_state =! LED_state;

​    digitalWrite(pin_LED, LED_state);



​    Serial.println(count);

​    count = 0;

  }

}

**
**

**
**

millis()

현재 시간ms로 리턴한다

unsigned long 타입으로 리턴 (2진수로 맨 앞이 부호비트, 1이면 음수, 0이면 양수)

아두이노는 리셋된 시점부터! 음수시간은 필요가 없기 때문에 0하고 양수만 쓸 것

unsigned는 과거 필요 없다

동시동작을 해야 하는데 delay 때문에 안 됐다

내가 직접 시간을 계산해서 처리해야 함



led가 가장 최근에 끄거나 키거나 했던 시간이 timepre, 이번 실행의 값  timecur

c-p 얼마나 시간이 흘렀나

count -> 1초 동안  loop 얼마나 도나

c-p -> 시간차

c-p >=1000이면 1초가 지났다면 루프 안으로 들어오기



p = c -> 이전 시간을 지금으로 업데이트, 기준 시간 업데이트



< ex11_2.ino > -> 동시에 다른 led를 시간차를 두고 깜빡이게 하기



int pin_LED1 = 7;

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

​    time_p1 = time_c1;

​    LED_state1 =! LED_state1;

​    digitalWrite(pin_LED1, LED_state1);

  }

}



void blink_500(){

  time_c2 = millis();

  if(time_c2 - time_p2 >= 500){

​    time_p2 = time_c2;

​    LED_state2 =! LED_state2;

​    digitalWrite(pin_LED2, LED_state2);

  }

}





**F1 -> arduino library -> simple timer 설치**

**혹은 github로 수동 설치 (문서 아래 라이브러리에 설치하면 된다)**

**
**

**
**

< ex11_3.ino > -> 동시에 다른 led를 시간차를 두고 깜빡이게 하기(SimpleTimer 사용)





\#include <SimpleTimer.h>



int pin_LED1 = 3;

int pin_LED2 = 7;

int pin_LED3 = 13;



SimpleTimer timer; // 정적할당, 전역영역에 할당



void blink_1000(){

  int state = digitalRead(pin_LED1); // 이 핀의 현재 상태 읽기

  digitalWrite(pin_LED1, !state);

}



void blink_500(){

  int state = digitalRead(pin_LED2);

  digitalWrite(pin_LED2, !state);

}



void blink_300(){

  int state = digitalRead(pin_LED3);

  digitalWrite(pin_LED3, !state);

}

void setup(){

  pinMode(pin_LED1, OUTPUT);

  pinMode(pin_LED2, OUTPUT);

  pinMode(pin_LED3, OUTPUT);

  timer.setInterval(1000, blink_1000);

  timer.setInterval(500, blink_500);

  timer.setInterval(300, blink_300);

}



void loop(){

  timer.run();

}



아날로그 출력 방식

디지털 출력을 조절해서 동일한 효과 구현



![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMTgz/MDAxNTk5ODA1OTIxNzQ1.UCRZ0E3gXWsfrDwjm8GvzmIDzkqeT5LUrQVytnlv9CIg.rep9y-16PDiQ-zW8zviBoRhM_a7tQ4g-6MG2oiaHQ7Yg.PNG.til_t/%EC%A0%9C%EB%AA%A9_%EC%97%86%EC%9D%8C.png)



PWM(Pulse width modulation) : 펄스 폭 변조 -> 펄스의 폭을 바꾸겠다(필요에 따라서 폭을 조정)

0(digitalWrite(led, low)), 1(digitalWrite(led, high)) -> 이 로우와 하이를 주기적으로 동일한 패턴으로 나가는 것을 펄스라고 부른다

빛의 밝기는 전기의 양에 의해서 결정이 난다

전기를 많이 받으면 밝게 빛나고 적게 받으면 어둡게 밝힌다

지금까지 한 디지털은 한 주기가 다 꽉 찼다, 100%high로 내보낸 것, 최대 밝기로

펄스의 폭이 길면 전기를 많이 내보낼 것이고 짧으면 전기를 적게 내보낼 것 

PWM 주파수 : 500HZ (1/500 = 0.002ms) 한 주기 당 2ms로 운영되고 있다



듀티비, 듀티사이클(Duty rate, Duty cycle)

analogWrite() -> 0~255 값 출력

analogWrite(255) : 항상 켜짐, 100%

analogWrite(127) : 50%

analogWrite(핀번호, 전압(0~255)) -> 아날로그 출력 핀의 전압을 설정하는 함수

틸트(~) 표시가 있는 핀을 사용(~3, ~5, ~6, ~9, ~10, ~11)



< ex12.ino >





int pin_LED = 3;



void setup(){

  pinMode(pin_LED, OUTPUT);

}



void loop(){

  for(int i = 0; i <= 255; i++){

​    analogWrite(pin_LED, i);

​    delay(20);

  }

  for(int i = 255; i >= 0; i--){

​    analogWrite(pin_LED, i);

​    delay(20);

  }

}

![img](https://ssl.pstatic.net/static.se2/static/img/alter_video.png)

< ex12_2.ino > -> 차례대로 밝아졌다가 어두워지는 예제







int pins[] = {3, 5, 6};



void setup(){

  for(auto &pin : pins){

​    pinMode(pin, OUTPUT);

  }

}



void fade(int pin){

  for(int i = 0; i <= 255; i++){

​    analogWrite(pin, i);

​    delay(10);

  }

  for(int i = 255; i>=0; i--){

​    analogWrite(pin, i);

​    delay(10);

  }

}

void loop(){

  for(auto &pin: pins){

​    fade(pin);

  }

}

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMTAy/MDAxNTk5ODA5MDEwMzMy.3Hrgl_xYfkjxOu5hc_oNEInHm4LV85U4epnWIQi6ERAg.4VeD_5MBus51yQNXViK8Z6m4pAgkVGyN2hZL9dvVMVgg.JPEG.til_t/P20200911_160331984_0299F47B-36CA-4DDC-94F5-238EA91CE7ED.jpg)

3색 ledR, G, B 핀에 0~255 사이의 값을 analogWrite()함수로 출력3색의 조합으로 색상 결정2번(다리 긴 것이 -), 1번 R, 3번 G, 4번 B
![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjI3/MDAxNTk5ODA4NTE1MjIx.zeWx4iEtcDuMzBsP6ftEjdFbur-QBmnMdLiFZoO6pCIg.EJwV2ao7ewrWzv9F7QrEEw-jOShXlETE1VRM-NAsOYIg.JPEG.til_t/P20200911_161001450_2EA0195C-8DCE-4905-A2BB-95D3DE3520AA.jpg)

**-를 GND에 연결하고 나머지 RGB를 순서대로 이어서 연결해준다****그 연결을 저항이 받아서 떨어져 있는 공간을 연결한다**

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjAw/MDAxNTk5ODA4NTIxMzc1.eO0W_ShK9thdE3eIrhKeCkhG_DzbPsF9EIKfaeksXRYg.XVnNYTw1fy-jjuXXGGwjkXheIorT5QDcpE5BM6wpfG0g.JPEG.til_t/P20200911_161343086_2B185BF5-5255-48D7-9C05-CEAA22AE3BDB.jpg)

< color_ledex_01.ino >

const int redPin = 11;const int greenPin = 10;const int bluePin = 9; // 틸트 핀을 써야 함
void setup(){  randomSeed(analogRead(A0)); // 0~1023을 리턴한다, 임의의 값을 지정하는 기법}
void loop(){  analogWrite(redPin, random(256));  analogWrite(greenPin, random(256));  analogWrite(bluePin, random(256));  delay(1000);}

![img](https://ssl.pstatic.net/static.se2/static/img/alter_video.png)

< color_ledex_01_2.ino > -> 선명하게 색깔 출력해보기

const int redPin = 11;const int greenPin = 10;const int bluePin = 9; // 틸트 핀을 써야 함
void setup(){  randomSeed(analogRead(A0)); // 0~1023을 리턴한다, 임의의 값을 지정하는 기법  analogWrite(redPin, 255);  delay(1000);  analogWrite(redPin, 0);  analogWrite(greenPin, 255);  delay(1000);  analogWrite(greenPin, 0);  analogWrite(bluePin, 255);  delay(1000);  analogWrite(bluePin, 0);}
void loop(){  analogWrite(redPin, random(256));  analogWrite(greenPin, random(256));  analogWrite(bluePin, random(256));  delay(1000);}

조금 더 선명한 3LED

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfNzcg/MDAxNTk5ODExMTQzMzIw.King9xL-UUjroGxas0yAFQ58ZJac1gQLVgpgw3lSQg0g.euHniHmmdb4IYevr0GrpWDbjZ0n663UslujdZtzXWo4g.JPEG.til_t/P20200911_164628326_C7C4114C-ED3B-498A-BAC6-5459057FB38E.jpg)

**점퍼선을 연결한다**



![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMzYg/MDAxNTk5ODExMTQzNzE1.NvblLXWWdBnvSvMtTyRXA88FuQiEBUrJUIMqBvBEU98g.D7BP4WrOYG6st5pc5ZineHPiaQ05YdEPFE9OdHSlw3Mg.JPEG.til_t/P20200911_164711369_1BFD6166-00F9-42CB-9E51-69A92B7C0151.jpg)

**- 있는 부분의 점퍼선을 바로 아두이노의 digital 13 옆에 있는 GND에 꼽는다**

**그리고 나머지 부분을 틸트 핀에 꼽는다**



![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMTEw/MDAxNTk5ODExMTQ0MTEy.g8_nqxSJH__5mFafWxS2baN9XuFbZE8Y3Ukmk_5DA0Ig.K1opS3Sk6An3HIxUJT4CP8xYkZdS5QvnX5pCTPU_AbUg.JPEG.til_t/P20200911_164713691_4C277601-F938-421F-AB05-E1B46149A6A2.jpg)

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjk1/MDAxNTk5ODExMTQ0NjIw.SaOQU2p6_w3GoYnUXcbh1EhLTN8zQmXEOJjR1bi0g9Ug.klVLHgslfuBJXoBRM7-egnfjUAt-KZXTVaNbNo3hzY8g.JPEG.til_t/P20200911_165453611_88DDCEA2-0D56-4FCE-8ECB-8B72001681E6.jpg)

이렇게 꼽고 아까의 예제를 실행하면 조금 더 선명한 빛을 볼 수 있다


 

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMTA0/MDAxNTk5ODEzMTcxNDUw.B4u61-uJ4vHr8NYKMVv19PKbYBhXwQ9uMfnbjoPvyTgg.pmUDr8PzKxeV0y-XvkgM1RqChrp_JnbJOJqgLtpYgY4g.JPEG.til_t/P20200911_170219395_A3983296-154F-4835-BA4D-C7212D569FF4.jpg)

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjYy/MDAxNTk5ODEzMTcxNzc2.5q3MzwIsUM8MEIOKUp-h5VrfOxx94mrWAm0h3IbzGNsg.SSLk1a9FAeweUB01wZU_f89gWOGXGPPlwVmmvnuLJKYg.JPEG.til_t/P20200911_170608074_5E813B32-7DA5-4398-A70E-A317A2494295.jpg)


1602 character LCD (한 줄에 16글자, 줄은 2줄)백라이트는 5V, 가변 저항으로 폰트의 명암을 조절

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjMg/MDAxNTk5ODEzMTcyMjIx.SjBcTgTDXU5Nl-tm5R8NrrGlEz0svBiJyjy72Q4hGaUg.Wx9vWX2hmxDtksPntwOxTxB_LgUF6GsI6dGIzD6DQlcg.JPEG.til_t/P20200911_170758604_1BB5FB6D-47EF-4D84-9B2D-5C760B4D32DE.jpg)


LCD interface ConverterI2C 인터페이스를 사용해서  LCD 제어단 4개의 선으로 LCD 조작점퍼 스위치 : LCD 백라이트 온오프 제어가변저항 : LCD 명암 조절I2C 주소 초기값 : 0x27 또는 0x3F

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjIy/MDAxNTk5ODEzMTcyNjA2.JYb_RZ1aRVlJsRsYf5vS3xFHmCRSOcoOPvFeQGOXZogg.NCIqrz_DeRhNqFto5wlZj43XL0cfCacBnal6OeAlMnog.JPEG.til_t/P20200911_170857517_D70582E1-73AB-4447-9123-A08DA50D81E3.jpg)


위의 두 개는 전원 (GND, VCC)SDA -> 데이터 왔다갔다하는 곳SCL -> Clock

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfNDEg/MDAxNTk5ODEzMTczMDEx.IAZ3DoxIpuS71cmyQDGZECmxZITgphX0vZfQD8Y3kvkg.pP2_9qp9c1qVsMGoA5L3k0AiVAISlkFJafDU5-6nAcEg.JPEG.til_t/P20200911_171306920_2A9B7F90-7C92-41C5-BE88-246662632B0A.jpg)


**GND -  아두이노의 밑쪽 GND****VCC - 아두이노의 밑쪽 5V****SDA - 아두이노 ANALOG IN의 A4****SCL - 아두이노 ANALOG IN의 A5**

![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMjUg/MDAxNTk5ODEzMTczNDkw.y67F4TMDQj4EzIc5NFmAprXzlQZigGUunZRpur4pt2Mg.pTYv09iCIojsd8KuRvGW7HvbZpAG5J4pN3DTqV-5aIwg.JPEG.til_t/P20200911_172355550_74C3B91D-95E9-4251-A03A-D81872FC1F7F.jpg)


[**https://github.com/johnrickman/LiquidCrystal_I2C**](https://github.com/johnrickman/LiquidCrystal_I2C)**LiquidCrystal_I2C 라이브러리 다운****
****
****lcd.init(); // LCD 초기화** **lcd.backlight(); // LCD 백라이트를 켠다** **lcd.noBacklight(); // LCD 백라이트를 끈다** lcd.noDisplay(); // LCD 표시된 내용을 숨긴다 lcd.display(); // LCD 표시내용을 보여준다 lcd.cursor(); // 커서를 표시한다 lcd.noCursor(); // 커서를 없앤다. **lcd.setCursor(0,0); // 해당 LCD 좌표로 커서 이동** lcd.home(); // 커서를 0,0 좌표로 이동 lcd.blink(); // 커서를 깜빡임 lcd.noBlink(); // 커서를 깜빡이지 않음 **lcd.write(36); // LCD 화면에 값 출력, 아스키코드 입력 시 해당문자 출력** **lcd.print("TEST"); // LCD 화면에 값을 출력** lcd.clear(); // LCD 모든 내용 지움 lcd.scrollDisplayRight(); // lcd 내용을 우측으로 1칸 스크롤 lcd.scrollDisplayLeft(); // lcd 내용을 좌측으로 1칸 스크롤 lcd.autoscroll(); // 출력내용을 자동으로 우에서 좌로 스크롤


< lcd_ex02.ino >



\#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup(){  lcd.init(); // LCD 초기화  lcd.backlight(); // 백라이트 켜기  lcd.setCursor(3, 0); // 커서 위치 설정 (x,y)
  // 문자열 출력  lcd.print("Hello, World!");}
void loop(){
}



![img](https://blogfiles.pstatic.net/MjAyMDA5MTFfMSAg/MDAxNTk5ODEzMTczOTM0.aowM4yGB-14FZOGnaaABR97Xo9GqgeG1IOdpILlIZHIg.x5_VRiNMltxXYy5QU5112Ql0fnhDERZpofNarbabqVMg.JPEG.til_t/P20200911_172732530_BAF60396-4F9F-4E2E-84DB-D77FF590EDC1.jpg)



위의 코드를 실행시키면 lcd에 원하는 좌표에 출력된다