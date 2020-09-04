class Parent {
    constructor(name) {
        this.name = name;
    }
    print() {
        console.log("이름 : " + this.name);
    }
}

class Child extends Parent {
    constructor(name, age) {
        super(name);
        this.age = age;
    }
    print() {
        super.print();
        console.log("나이 : " + this.age);
        //오버라이드 -> 재정의
    }
    static sayHello() {
        console.log('Hello~');
    }
}

class GrandChild extends Child {
    constructor(name, age, address) {
        super(name, age);
        this.address = address;
    }
    print() { 
        super.print(); 
        console.log("주소 : " + this.address);
    }
}
var person = new GrandChild("홍길동", 20, "서울");
person.print();
GrandChild.sayHello();

// 그랜드차일드의 수퍼는 차일드, 차일드의 수퍼는 페어런트
// babel이라는 툴로 예전 걸로 바꾸는 툴이 있음 그걸로 최신 버전을 예전 것으로 바꿔서 사용