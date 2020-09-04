// __init__ 생성자 함수와 같은 게 constructor

class Student{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    // 프로토타입 표시 안 해도 자동으로 프로토타입 함수로 넘어간다
    printProfile(){ // function키워드 안 붙음!
        console.log(`이름 : ${this.name}, 나이 : ${this.age}`);
    }
}

var s1 = new Student("원종아", 25);
console.log(s1.name);

s1.printProfile();

console.log("printProfile" in s1.__proto__);
// 프린트프로파일이 프로토에 있냐 트루 있다
console.log("printProfile" in Student.prototype);
// 스튜던트의 프로토타입에 있냐 있다