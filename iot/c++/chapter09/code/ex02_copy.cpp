#include <iostream>
#include <string>
using namespace std;

class MyArray{
    public:
    int size;
    int *data;

    MyArray(int size){
        this->size = size;
        data = new int[size];
    }
    
    MyArray(const MyArray& other){
        size = other.size;
        data = new int[other.size];
        for(int i = 0; i < size; i++){
            data[i] = other.data[i]; // 복사 생성자 호출
        }
    }
    ~MyArray(){
        if(data != NULL){
            delete []data;
        }
    }
};

int main(int argc, char const *argv[]) {
    MyArray buffer(10);
    buffer.data[0] = 1;
    {
        MyArray clone = buffer; // 복사 생성자 호출, 문제가 되는 곳
    } // clone 삭제

    buffer.data[0] = 2; // 이 연산을 보장하지 못함
    return 0;
}