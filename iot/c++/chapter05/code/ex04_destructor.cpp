#include <iostream>
#include <string.h>
using namespace std;

class MyString{
    private:
    char *s;  // 포인터
    int size;

    public:
    MyString(char *c){
        size = strlen(c) + 1;
        s = new char[size];  // 동적할당
        strcpy(s, c);
    }
    ~MyString(){
        cout << "~MyString ... delete s" << endl;
        delete[]s;
    }
};

int main(int argc, char const *argv[]) {
    MyString str("abcdef");
    return 0;
}