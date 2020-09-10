#include <string>
#include <iostream>
using namespace std;

class Rectangle{
    private:
    int length;
    int width;

    public:
    // Rectangle(int length = 30, int width = 40){
    //     this->length = length;
    //     this->width = width;
    // }

    Rectangle(int length = 30, int width = 40)
        : length(length), width(width){
            // this를 안 써도 멤버인지 매개변수인지 알 수 있다
        }
    ~Rectangle(){}
    void setLength(int length){this->length = length;}
    int getLength() {return this->length;}
    void setWidth(int width){this->width = width;}
    int getWidth(){return this->width;}
};

int main(int argc, char const *argv[]) {
    Rectangle rect(50,60);

    cout << "length : " << rect.getLength() << endl;
    cout << "width : " << rect.getWidth() << endl;

    rect.setLength(20);
    rect.setWidth(10);

    cout << "length : " << rect.getLength() << endl;
    cout << "width : " << rect.getWidth() << endl;

    return 0;
}