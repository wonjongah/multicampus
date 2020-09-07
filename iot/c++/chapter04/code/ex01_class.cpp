#include <iostream>
#include <string>
using namespace std;

class Circle{
    // public:
    private: // 클래스 밖에서 사용하려고 할 때 문제가 생긴다
    int radius;
    public:
    string color;
    public:
    double calcArea(){ // 파이썬과 달리 self 매개 변수 없다
        return 3.14 * radius * radius;
    }
};

int main(int argc, char const *argv[])
{
    Circle obj; // 객체 생성
    obj.radius = 100;  
    obj.color = "blue";
    // obj.area = 40; // 에러 -- 동적으로 멤버 추가 불가

    cout << "area : " << obj.calcArea() << endl;
    return 0;
}
