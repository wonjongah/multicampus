#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
    string s1, addr;

    cout << "name : ";
    cin >> s1;
    // cin.ignore(); // 엔터키 제거
    // 주소는 공백이 들어가니 

    cout << "address : ";
    getline(cin, addr);

    cout << addr << "'s " << s1 << " sir hello" << endl;

    return 0;
}