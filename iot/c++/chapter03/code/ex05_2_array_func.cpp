#include <iostream>
using namespace std;


void initArray(int array[], int size, int value = 0){
// int value = 0는 call by value, & 없기 때문, 대입연산을 통해서 값이 대입될 수 있어야 한다
// int array[] -> 비워두면 초기화식의 엘리먼트의 개수에 따라 결정된다, 범용함수
// 호출될 때 결정된다, 배열의 크기 한정짓지 않았다
    // int size = sizeof(array) / sizeof(int);

    for (int i = 0; i < size; i++){
        array[i] = value;
    }
}

void printArray(int array[], int size){
    
    // int size = sizeof(array) / sizeof(int);

    for(int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(int argc, char const *argv[]) {
    int intList[10];

    initArray(intList,10, 100); // 두 번째 인자 값으로 초기화
    printArray(intList, 10);
    initArray(intList, 10); //인자 하나, 0으로 초기화
    printArray(intList, 10);
    return 0;
}