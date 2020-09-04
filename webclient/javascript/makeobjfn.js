function Student(name, korean, math, english, science) {
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;

    this.getSum = function() {
    return this.korean + this.math + this.english + this.science;
    }
    this.getAverage = function() {
    return this.getSum() / 4;
    }
    this.toString = function() {
    return `${this.name}\t${this.getSum()}\t${this.getAverage()}`;
    }
    };

    // new가 의미하는 게 정확하게 새로운 객체를 위한 인스턴스를 만들고 나서 이 함수 호출
    // 이 함수 호출 당시에 this라는 애가 새로 만든 인스턴스가 참조되도록 해준다
    // 리턴은 디스의 값이 리턴이 된다
    // new -> 새로운 객체를 위한 힙을 만들어라!!!!!!!
   var student = new Student("김세진", 45, 67, 56, 34);
    console.log(student);
    var student2 = Student("킴세진", 22, 22, 33, 22);
    console.log(student2);
    // new 안 쓰면 undefined


    
    var students = [];
students.push(new Student('윤인성', 90, 83, 76, 89));
students.push(new Student('박찬호', 90, 83, 76, 89));
students.push(new Student('류현진', 90, 83, 76, 89));
students.push(new Student('이세돌', 90, 83, 76, 89));
students.push(new Student('김세진', 90, 83, 76, 89));
students.push(new Student('이하나', 90, 83, 76, 89));
var output ='name\t총점\t평균\n';
for(var i in students) {
output += students[i].toString()+ '\n';
}
console.log(output);