#include <string>
#include <iostream>
#include <memory>
using namespace std;

class Dog{
    public:
    int age;
    string name;

    Dog(){
        cout << "Dog constructor" << endl;
        age = 1;
        name = "바둑이";
    }
    
    ~Dog(){
        cout << "Dog destructor" << endl;
    }

    int getAge() {return age;}
    void setAge(int a) {age = a;}
};
int main(int argc, char const *argv[]) {
    // Dog *pDog = new Dog;
    // delete pDog;

    unique_ptr<Dog> dog(new Dog);

    cout << "age : " << dog->getAge() << endl;
    dog->setAge(3);
    cout << "age : " << dog->getAge() << endl;

    return 0;
}