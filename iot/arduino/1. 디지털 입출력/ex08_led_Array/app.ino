int pins[] = {3, 5, 7, 9};
int state = 0;

void setup(){
    Serial.begin(9600);
    for(int i = 0; i < 4; i++){
        pinMode(pins[i], OUTPUT);
        digitalWrite(pins[i], LOW);
    }
}

void loop(){
    for(int i = 0; i < 4; i++){ // 0 X X X 
        if(i==state){
            Serial.print("0 ");
            digitalWrite(pins[i], HIGH);
        } else{
            Serial.print("X ");
            digitalWrite(pins[i], LOW);
        }
    }
    Serial.println();
    state = (state + 1) % 4; // 0~3
    delay(1000);
}