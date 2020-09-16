const int ledPin = 13;
const int inputPin = 11;
void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT_PULLUP); // 내부 풀업 스위치
}
void loop() {
    int swInput = digitalRead(inputPin);
    if (swInput == LOW) // 스위치를 누르면
        digitalWrite(ledPin, HIGH);
    else
        digitalWrite(ledPin, LOW);
}