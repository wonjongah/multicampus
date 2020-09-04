#include <iostream>
using namespace std;

int main(int arg, char const *argv[]){
    bool b;
     
    b = (1 == 2);

    cout << std::boolalpha;
    // 설정을 바꾸겠다
    // bool을 숫자 말고 true, false로 출력하도록 설정을 바꾸겠다
    cout << b << endl;

    return 0;
    
}