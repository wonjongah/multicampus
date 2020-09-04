var human = {
    name: "김상형",
    age: 29,
    score1: 99,
    score2: 88,
    score3: 82 
};

var h = human;
// 참조를 같은 곳을 하는 것, 같은 인스턴스 가리킴
// 참조를 복사하는 것이지 복사의 기능이 아님
for(var i = 1; i <= 3; i++){
    console.log(i + "학년 성적 = " + h["score" + i] + "점");
}

h.name = "김태희"; // 원본 바뀜
// 객체를 매개변수로 넘긴다, 콜바이레퍼런스, 원본으로 작업을 하는 것
// 대입.. 값이 복사되는 것이 아님!!
console.log("name = " + h.name);
console.log("age = " + h.age);

// for문을 써서 다 출력하고 싶을 때 . 말고 []를 써서 