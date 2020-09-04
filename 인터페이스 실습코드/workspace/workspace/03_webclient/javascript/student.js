class Student{
    constructor(name, age){
        this._name = name;
        this.age = age;
    }

    printProfile(){ // function키워드 안 붙음!
        console.log(`이름 : ${this.name}, 나이 : ${this.age}`);
    }

    get name(){
        return this._name;
    }
    
    set name(name){
        this._name = name;
    }
}

var s1 = new Student("홍길동", 20);
console.log(s1.name);
s1.name = '고길동'
console.log(s1.name);
console.log(s1);

// 스태틱엔 디스를 쓸 수 없다, 파이썬이었으면 셀프를 쓸 수 없다

// 파이썬은 class Child(Parent)이렇게 씀, 자스는 괄호 대신 extends
