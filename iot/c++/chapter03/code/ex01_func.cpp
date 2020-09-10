#include <iostream>
using namespace std;

// 함수의 존재 밝혀준다, 함수 원형, 뒤에 나올 것이다
int max(int x, int y); 

int max(int x, int y){
    if (x > y){
        return x;
    }
    else
    {
        return y;
    }
    
}

int main(int argc, char const *argv[]) {
    int n;
    n = max(2,3);
    // 함수를 정의 전에 호출해도 요즘 컴파일러는 돌아간다
    cout << "result : " << n  << endl;

    return 0;
}