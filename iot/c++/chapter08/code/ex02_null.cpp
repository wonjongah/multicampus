#include <iostream>
using namespace std;

void f(int i){
    cout << "f(int)" << endl;
}

void f(char *p){
    cout << "f(char *)" << endl;
}

int main(int argc, char const *argv[]) {
    //f(NULL); -> int, char * 둘 다 가능하므로 에러
    // f(nullptr); // nullptr: 포인터 NULL을 의미하는 키워드 

    int *pNumber = NULL; // 권장
    int *pNumber2; // 권장하지 않음
    // 무슨 값이 들어있는지 모른다! 임의의 초기값을 가짐

    if(pNumber != NULL){
        cout << *pNumber << endl;
    }   

    if(pNumber2 != NULL){
        cout << *pNumber2 << endl;
    }
    f(nullptr);
    f(0);
    return 0;
}