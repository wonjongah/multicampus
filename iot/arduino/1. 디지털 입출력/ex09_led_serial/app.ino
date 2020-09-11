int pin_LED = 13; // 특수하게 보드에 있는 led로 출력 가능

void setup(){
    Serial.begin(9600);
    pinMode(pin_LED, OUTPUT);
}

void loop(){
    if(Serial.available()){ // 수신된 데이터가 있냐
        char inChar = Serial.read(); // read() 글자 하나를 읽는다
        if(inChar == '\r' || inChar == '\n'){
            return;
        }
        if(inChar == '1'){ // 문자 1이면 불을 키겠다
            digitalWrite(pin_LED, HIGH);
        }
        else{
            digitalWrite(pin_LED, LOW);
        }
    }
}