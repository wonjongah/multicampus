#include <iostream>
using namespace std;

void display(char c = '*'){
    for (int i = 0; i < 20; i++){
        cout << c;
    }
    cout << endl;
}
void display(char c = '*', int n = 10){
    for (int i = 0; i < n; i++){
        cout << c;
    }
    cout << endl;
}

int main(int argc, char const *argv[]) {
    display();          // 허용 X, 둘 다 호출가능한 형태
    display('#');       // 허용 X, 둘 다 호출가능한 형태
    display('#', 5);     //후자의 display
    return 0;
}