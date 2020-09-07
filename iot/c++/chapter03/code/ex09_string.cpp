#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
    
    string s = "when in rome, do as the romans";

    // 읽기

    for(auto& ch : s){  // char &ch = s[i], 참조, 속도 더 빠름
        cout << ch << ' ';
    }
    cout << endl;
    for (auto ch : s){  // char ch = s[i], 새로운 변수 만들고 값 복사
        cout << ch << ' ';
    }
    cout << endl;

    // 읽을 때는 참조변수로 하나 값 복사하나 결과 똑같다

    // 쓰기 (참조와 값복사가 다름)

    for(auto& ch : s){  // char &ch = s[i], 이름만 추가, T를 위한 공간 할당 X, 원본으로 작업
        ch = 'T';
    }
    cout << s << endl;

    for (auto ch : s){  // char ch = s[i], ch를 위한 별도의 메모리 공간을 만들고 운영(1byte), 값 복사
        ch = 'W'; // 메모리 공간에 W 입력
    }
    cout << s << endl; // 원본에는 변화 X
    // 쓰기 작업은 속도의 문제가 아니라 원본을 수정할 것인지 아닌지의 문제
    // 속도 자체는 참조변수가 더 빠르다

    return 0;
}