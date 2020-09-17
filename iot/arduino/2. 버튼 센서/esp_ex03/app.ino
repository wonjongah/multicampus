#include "WifiUtil.h"

const char SSID[] = "KT_WiFi_2G_3AAD";
const char PASSWORD[] = "0bi64if392";
const char server[] = "arduino.cc";

WifiUtil wifi(2, 3);
WiFiEspClient client;

void setup(){
    Serial.begin(9600);
    wifi.init(SSID, PASSWORD);
    request();
}

void loop(){ 
    response();
}


void request() {
    // if you get a connection, report back via serial
    if (client.connect(server, 80)) {
        Serial.println("Connected to server");
        // Make a HTTP request
        client.println("GET /asciilogo.txt HTTP/1.1"); // get이기 때문에 바디 없다
        client.println("Host: arduino.cc"); // 헤더
        client.println("Connection: close"); // 헤더
        client.println();
    }
}
void response() {
    while (client.available()) {
        char c = client.read();
        Serial.write(c);
    }
}