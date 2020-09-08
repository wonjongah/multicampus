#include <iostream>
using namespace std;

class Second{
    public:
    int sec;

    Second(){
        sec = 0;
    }
    Second(int s){
        sec = s;
    }
};

// Second second;  // 디폴트 생성자
// Second second(20);  // 매개변수 1개인 생성자

class Time{
    public:
    int hour;
    int minute;
    Second sec;

    Time() : sec(20){ // Second sec(20);과 같음
        hour = 0;
        minute = 0;
        sec = sec;
    }

    // Time(int h, int m){
    //     hour = h;
    //     minute = m;
    // }
    Time(int h, int m) : hour(h), minute(m), sec(20){}

    void print(){
        cout << hour << ":" << minute << endl;
    }
};

int main(int argc, char const *argv[]) {
    Time a;
    Time b(10, 25);
    Time c{10, 25};
    Time d = {10, 25};
    
    b.print();
    c.print();
    d.print();

    return 0;
}