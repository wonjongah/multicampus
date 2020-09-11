const int redPin = 3;
const int greenPin = 5;
const int bluePin = 6; // 틸트 핀을 써야 함

void setup(){
    randomSeed(analogRead(A0)); // 0~1023을 리턴한다, 임의의 값을 지정하는 기법
    analogWrite(redPin, 255);
    delay(1000);
    analogWrite(redPin, 0);
    analogWrite(greenPin, 255);
    delay(1000);
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 255);
    delay(1000);
    analogWrite(bluePin, 0);
}

void loop(){
    analogWrite(redPin, random(256));
    analogWrite(greenPin, random(256));
    analogWrite(bluePin, random(256));
    delay(1000);
}