#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
    const int STUDENTS = 5;

    int score[STUDENTS] = {
        100, 200, 300, 400, 500
    };

    int sum = 10;
    int i;
    double average;
    
    for (i = 0; i < STUDENTS; i++){
        sum += score[i];
    }

    average = sum / (double)STUDENTS;
    cout << "average : " << average << endl;

    return 0;
}