int pins[] = {3, 5, 7, 13};
int state = 0;

void setup(){
    Serial.begin(9600);
    for(int i = 0; i < 4; i++){
        pinMode(pins[i], LOW);
    }
}

void loop(){
    if(Serial.available()){
        char data = Serial.read();
        if(data == '\r' || data == '\n'){
            return;
        }
        Serial.println(String("You entered \'") + data + '\'');

        if(data >= '1' && data <= '4'){
        state = data - '0' - 1; // LED 인덱스 변환, 대상이 되는 인덱스 결정
        // data는 문자 코드 실제 숫자로 90이라고 가정해보자, 난 필요한 게 실제 숫자 1이 필요하다
        // int()와 같은 과정
        // '1'(90) - '0'(89) = 1
        // 0으로 만들기 위해 1을 뺀 것
        // 입력한 문자열 데이터를 실제 led의 숫자로 바꾸기 위한 연산
        Serial.print("LED ");
        Serial.print(state + 1);
        Serial.println("   i On... ");
        }else
        {
            Serial.println("* Invalid LED number ... ");
            state = -1;
        }
        for(int i = 0; i < 4; i++){
            if(i == state){
                Serial.print("0 ");
                digitalWrite(pins[i], HIGH);
            }else
            {
                Serial.print("X ");
                digitalWrite(pins[i], LOW);
            }
            
        }
        Serial.println();
        }
    
    
}