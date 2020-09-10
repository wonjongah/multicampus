
#include <TrafficLight.h>

TrafficLight lights(7, 6, 5); // 전역변수로 만들고 핀의 번호 넘겨준다

void setup()
{
    
}



// 2초간 직진 신호
// 1초간 직진, 좌회전 신호
// 2초간 직진 및 좌회전 블링크
// 2초간 정지 신호
void loop()
{
    lights.run();
}
