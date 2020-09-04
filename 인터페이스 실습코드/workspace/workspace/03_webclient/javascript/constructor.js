function Student(name, korean, math, english, science) {
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;
    }

// 클래스명.프로토타입.함수명

Student.prototype.getSum = function(){
    return this.korean + this.math + this.english + this.science;    
}

Student.prototype.getAverage = function(){
    return this.getSum / 4;
}

// 스투던트 인스턴스 아님, 스투던트 안에 프로토타입이 참조하는 오브젝트에 겟썸, 겟..있음

Student.prototype.toString = function(){
    return `${this.name}\t${this.getSum()}\t${this.getAverage()}`;
}

// s1 = new Student()
// s1.xxx xxx는 먼저 가지고 있는 걸 찾음 없음? 그러면 __proto__를
// 따라가 가리키고 있는 오브젝트를 뒤짐, 없으면 또 그의 프로토타입...
// 그러다가 없으면 언디파인드
// 인스턴스는 여러개가 있지만 프로토가 가리키는 객체는 한 개로 구성
// 그 프로토가 가리키는 객체는 공유해서 씀
