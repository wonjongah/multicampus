#include "WifiUtil.h"

const char SSID[] = "KT_WiFi_2G_3AAD";
const char PASSWORD[] = "0bi64if392";

WifiUtil wifi(2, 3);

void setup(){
    Serial.begin(9600);
    wifi.init(SSID, PASSWORD);
}

void loop(){  // 루프문에서 와이파이 항상 체크
    if(wifi.check()){ // wifi 연결 확인, 0(끊긴 적 없었다), 1(끊겼다가 다시 연결)
        ; // 끊겼다가 다시 연결
    } // 네트워크 활용하는 코드는 여기에 기입, 네트워크 연결 보장하는 곳
}