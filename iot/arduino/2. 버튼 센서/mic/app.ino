int Led = 13; // define LED Interface
int buttonpin = 3; // define D0 Sensor Interface
int val; // define numeric variables val
void setup() {
    pinMode(Led, OUTPUT); // define LED as output interface
    pinMode(buttonpin, INPUT); // output interface D0 is defined sensor
}
void loop() {
    val = digitalRead(buttonpin);
    if (val == HIGH) {
        digitalWrite(Led, HIGH);
    } else {
        digitalWrite(Led, LOW);
    }
}