#include <iostream>
using namespace std;

class Pizza{
    public:
    int size;
    Pizza(int s) : size(s){}
};

Pizza makePizza(){ // factory 함수, 객체 반환
    Pizza p(10);
    return p; // p는 makePizza가 끝날 때 사라진다
}
int main(int argc, char const *argv[]) {
    
    Pizza pizza = makePizza(); // 생성자 호출이 아니라 오른쪽 함수로 초기화하겠다

    cout << pizza.size << "인치 피자" << endl;
    
    return 0;
}