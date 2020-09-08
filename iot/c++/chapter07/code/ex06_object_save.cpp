#include <vector>
#include <iostream>
using namespace std;

class Circle{
    public:
    int x, y;
    int radius;

    Circle() : x(0), y(0), radius(0){}
    Circle(int x, int y, int r) : x(x), y(y), radius(r){}

    void print(){
        cout << "radius : " << radius << " @(" << x << "," << y << ")" << endl;
    }
};
int main(int argc, char const *argv[]) {
    
    vector<Circle> objArray; // 벡터타입으로 지역변수

    for (int i = 0; i < 10; i++){
        Circle obj{rand() % 300, rand() % 300, rand() % 100};
       // 지역변수, for문 한 번 돌면 사라진다, for문 안에 선언됐기 때문에
        objArray.push_back(obj); // 루프 돌 때마다 힙에 생긴다
        // objArray는 힙을 가리킨다
    }

    for(auto &c: objArray){ // 힙을 순서대로 가리킴
        c.print();
    }
    return 0;

    // 스택만 지워서 될 일이 아니라 힙에 있는 메모리도 지워줘야 한다
    // vector에 파괴자(~vector)가 있어서 objArray가 소멸될 때(메인함수 끝날 때), 알아서 힙의 데이터도 지워준다
}