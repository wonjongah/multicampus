#include <iostream>
using namespace std;

class Shape{
    protected:
    int x, y;
    public:
    void draw(){}
    void move(){}
};

class Rectangle: public Shape{
    protected:
    int width, height;
    public:
    int calcArea(){
        return width * height;
    }
};

int main(int argc, char const *argv[]) {
    
    return 0;
}