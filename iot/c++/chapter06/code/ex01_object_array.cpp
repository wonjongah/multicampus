#include <iostream>
using namespace std;

class Circle{
    public:
    int x, y;
    int radius;

    Circle(): x(0), y(0), radius(0){}
    Circle(int x, int y, int r): x(x), y(y), radius(r){}
    void print(){
        cout << "radius : " << radius << " @{" << x << "," << y << ")" << endl;
    }
};
int main(int argc, char const *argv[]) {
    Circle objArray[10];  // 10개의 요소가 디폴트 생성자에 의해 생성, 중요, 정적할당, objArray는 상수

    for(Circle c: objArray){  // 디폴트 생성자로 0이 출력된다
        c.print();
    }

    for(Circle& c: objArray){
        c.x = rand() % 500;  // 0<= c.x < 500
        c.y = rand() % 300;  // 0<= c.y < 300
        c.radius = rand() % 100;  // 0 <= c.radius < 100
    }

    for(Circle c: objArray){
        c.print();
    }

    cout << "Circle memory : " << sizeof(Circle) << endl;  // int(4byte) * 3개
    cout << "array length : " << sizeof(objArray) << endl;
    return 0;
}