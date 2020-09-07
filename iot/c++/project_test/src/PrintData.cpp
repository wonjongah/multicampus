#include "PrintData.hpp"
#include <iostream>

void PrintData::print(int i){
    cout << i << endl;
}

void PrintData::print(double f){
    cout << f << endl;
}

void PrintData::print(string s){ // 디폴트 값 지정은 헤더파일에서만 지정
    cout << s << endl;
}