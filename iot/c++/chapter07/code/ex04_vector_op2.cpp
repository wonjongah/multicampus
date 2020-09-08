#include <vector>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    vector<int> v;
    for(int i=0; i<10; i++){
        v.push_back(i);
    }
    for(auto& e: v){
        cout << e<< " ";
    }
    cout << endl;

    cout << "delete" << endl;

    while(v.empty() != true){
        cout << v.back() << " "; // 마지막의 요소 출력하고 제거하는 while문
        v.pop_back();
    }

    cout << endl;

    cout << "size : " << v.size() << endl;
    cout << "capacity : " << v.capacity() << endl;
    
    return 0;
}