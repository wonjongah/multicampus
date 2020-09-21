#include <SoftwareSerial.h>
#include <WiFiEsp.h>
#include <PubSubClient.h>
#include <SimpleTimer.h>
#include <WifiUtil.h>

// SoftwareSerial softSerial(2, 3); // RX, TX
const char ssid[] = "KT_WiFi_2G_3AAD"; // 네트워크 SSID
const char password[] = "0bi64if392"; // 비밀번호
const char mqtt_server[] = "172.30.1.44"; // 서버 주소
// MQTT용 WiFi 클라이언트 객체 초기화
WifiUtil wifi(2,3);

WiFiEspClient espClient;
PubSubClient client(espClient);
SimpleTimer timer;

// sub
void callback(char* topic, byte* payload, unsigned int length) {
    payload[length] = NULL;
    char *message = payload;
    if (strcmp("1", message) == 0) { // 문자열로서 1이냐, string compare, 두 값이 같으면 0, 앞이 크면 양수, 뒤가 크면 음수
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
    Serial.print(topic);
    Serial.print(" : ");
    Serial.println(message);
}

void mqtt_init() {
    client.setServer(mqtt_server, 1883);
    // subscriber인경우 메시지 수신시 호출할 콜백 함수 등록
    client.setCallback(callback);
}

// MQTT 서버에 접속될 때까지 재접속 시도
void reconnect() {
    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        if (client.connect("ESP8266Client")) {  // 클라이언트아이드는 보통 시리얼 넘버로
            Serial.println("connected");
            // subscriber로 등록
            client.subscribe("home/livingroom/led"); // 연결이 됐으면 구독신청, 구독자 되는 방법
        } else { // 연결 안 되면 아무것도 안 한다
            Serial.print("failed, rc=");
            Serial.print(client.state()); // 실패 이유
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void publish() {
    int state = !digitalRead(13);
    char message[10];
    sprintf(message, "%d", state); // 현재 13번 led의 상태를 message로 보냄
    // 토픽 발행
    client.publish("home/livingroom/led", message);
}


void setup() {
    wifi.init(ssid, password);
    mqtt_init();
    Serial.begin(9600); // PC와 통신
    
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);
    timer.setInterval(2000, publish); // 2초 간격으로 퍼블리시
}


void loop() {
    if (!client.connected()) { // MQTT연결이 안 되어 있으면 재연결
        reconnect();
    }
    client.loop(); // 수신 메시지 있는지 없는지 확인하는 루프
    timer.run();
}