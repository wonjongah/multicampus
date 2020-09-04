#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    const int STUDENTS = 10;

    int scores[STUDENTS];
    int sum = 0;
    int i, average;
    for(i = 0; i < STUDENTS; i++){
        cout << "score : " ;
        cin >> scores[i];
    }
    for(i = 0; i < STUDENTS; i++){
        sum += scores[i];
     }

     average = sum / STUDENTS;
     cout << "average = " << average << endl;
    return 0;
}