int LED = 13;
int BUTTON = 11;
void setup() {
    pinMode(BUTTON, INPUT);
    pinMode(LED, OUTPUT);
}
// 풀업 평상시에 high
void loop() {
    if (digitalRead(BUTTON) == LOW) { // 누른 경우
        digitalWrite(LED, HIGH);
    } else {
        digitalWrite(LED, LOW);
    }
    delay(10);
}