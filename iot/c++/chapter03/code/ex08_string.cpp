#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
    string s = "when in rome, do as the romans";

    int size = s.size();
    int index = s.find("rome");

    cout << size << endl;
    cout << index << endl;
    cout << sizeof(s) << endl;
    
    return 0;
}