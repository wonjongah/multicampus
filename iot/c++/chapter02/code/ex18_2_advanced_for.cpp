#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    int list[] = {1,2,3,4,5,6,7,8,9,10};
    int list2[10];

    // int 하나는 4byte
    int length = sizeof(list) / sizeof(int); // 40 / 4 -> 10 (엘리먼트 개수)
    //   list 메모리 크기 :  int 크기(4) * 10개 -> 40byte
    cout << length << endl;;

    // 복사 전 list2 출력
    for(auto i: list2){
        cout << i << " ";
    }

    // 복사
    for (int i = 0; i < length; i++){
        list2[i] = list[i];
    }

    // 복사 후 lsit2 출력
    for(auto i: list2){
        cout << i << " ";
    }

    cout << list <<endl;


    return 0;

}