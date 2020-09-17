#include <SoftwareSerial.h>
#define BT_RXD 2
#define BT_TXD 3

SoftwareSerial softSerial(BT_RXD, BT_TXD);
void setup() {
  Serial.begin(9600); // PC와 통신
  softSerial.begin(9600);
  // 펌웨어로 설정된 디폴트 속도는 115200 bps
  softSerial.setTimeout(5000);
  delay(1000);
}

void loop() {
  if(Serial.available()){
    softSerial.write(Serial.read()); // PC로부터 온 데이터를 ESP로 보내겠다
  }
  if(softSerial.available()){
    Serial.write(softSerial.read()); // ESP로부터 받은 데이터를 PC로 보내겠다
  }

}
