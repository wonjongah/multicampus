#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int number = 0;
    int *p = &number;

    cout << p << endl;  // 주소 출력
    cout << *p << endl;  // 주소가 가지고 있는 값을 출력

    return 0;
}