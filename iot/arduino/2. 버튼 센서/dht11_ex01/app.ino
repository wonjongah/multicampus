#include <DHT.h>
#include "MiniCom.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht11(DHTPIN, DHTTYPE); // DHT 설정 - dht11(디지털2, dht11)

MiniCom com;

void checkHumiTemp(){
    float h = dht11.readHumidity();  // 습도값
    float t = dht11.readTemperature();  // 온도값

    com.print(0, "Humi", h);
    com.print(1, "Temp", t);
}

void setup(){
    com.init();
    com.setInterval(2000, checkHumiTemp);
    com.print(0, "MiniCom Start...");
    com.print(1, "Humi/Temp ex");
    // Serial.begin(9600);  // 9600 속도로 시리얼 통신 시작
    dht11.begin();
}

void loop(){
    com.run();
}