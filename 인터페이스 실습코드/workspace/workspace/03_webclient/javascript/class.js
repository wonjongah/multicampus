function Student(name, korean, math, english, science){
    this.name = name;
    this.korean = korean;
    this.math = math;
    this.english = english;
    this.science = science;
}

var student1 = new Student("김세진", 90, 85, 33, 66);
// new 없으면 undefined된다

console.log(student1.name);