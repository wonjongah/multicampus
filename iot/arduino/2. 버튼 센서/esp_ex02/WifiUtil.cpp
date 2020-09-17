#include "WifiUtil.h"

WifiUtil::WifiUtil(int rx, int tx): softSerial(rx, tx){

}

// 쉴드 존재 유무 확인

void WifiUtil::checkShield(){
    if(WiFi.status() == WL_NO_SHIELD){
        Serial.println("WiFi shield not present");
        while(true);
    }
}

// 와이파이 접속여부 확인 - 미접속이면 접속 시도
int WifiUtil::check() {
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print("Attempting to connect to WPA SSID: ");
        Serial.println(ssid);
        status = WiFi.begin(ssid, password);
        if (status == WL_CONNECTED) {
            printInfo();
            return 1; // 끊겼다가 다시 접속
            // 0을 리턴하면 끊긴 적 없음, 1리턴하면 끊겼다가 다시 리턴
        }
    }
    return 0; // 끊긴적 없음
}

void WifiUtil::init(const char *ssid, const char *password){
    this->ssid = ssid;
    this->password = password;

    softSerial.begin(9600);
    WiFi.init(&softSerial);

    checkShield();
    check();
}

void WifiUtil::printInfo() {
    // 와이파이 접속정보
    Serial.println("You're connected to the network");
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);
    long rssi = WiFi.RSSI();
    Serial.print("Signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
    Serial.println();
}