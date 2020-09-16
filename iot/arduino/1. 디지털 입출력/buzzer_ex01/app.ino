int buzzerPin = 5;

void setup(){
    pinMode(buzzerPin, OUTPUT);
}

void loop(){
    digitalWrite(buzzerPin, HIGH); // HIGH 소리남
    delay(1000);
    digitalWrite(buzzerPin, LOW);
    delay(1000);
}