#include <iostream>
#include <string>

#include "Car.hpp"
#include "PrintData.hpp"
using namespace std;

void printCar(Car car){
    cout << car.getSpeed() << endl;
    car.setSpeed(20);
}

int main(int argc, char const *argv[])
{
    Car myCar;

    myCar.setSpeed(100);
    printCar(myCar); // call by value
    
    cout << "speed : " << myCar.getSpeed() << endl;

    PrintData pd;

    pd.print(10);
    pd.print(10.2);
    pd.print("Hello World");
    pd.print();

    return 0;
}
