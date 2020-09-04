//  명시적 변환
//  Number() 관례로 보면 클래스.. 사실은 객체임
//  숫자로 변환할 수 있는 건 변환하고 못하는 것은 NaN
// parseInt() 인티저로 변환
// parseFloat() 실수로 변환

var korean = "82";
var english = "75";
var total = korean + english;
console.log("총점은 " + total + "이다.");

// 못 얻는다 변환해야 함!! 문자열 플러스니 붙여쓰기로 된다

var korean = "82";
var english = "75";
var total = Number(korean) + Number(english);
console.log("총점은 " + total + "이다.");

var korean = "82점";
var english = "75점";
var total = Number(korean) + Number(english);
console.log("총점은 " + total + "이다.");
// NaN이 나온다.. 

var korean = "82점";
var english = "75점";
var total = parseInt(korean) + parseInt(english);
// parseInt는 변환할 수 없는 값이 나오면 그대로 멈춤
// 숫자 변수는 그래서 이걸 더 많이 쓴다
console.log("총점은 " + total + "이다.");

// String() -> 숫자를 문자열로 변환

var staff = "김상형 : ";
var salary = 320;
var bonus = 160;

console.log(staff + salary + bonus + "만원");
// 왼쪽부터 더하기 문자열 + 숫자니까 숫자가 문자열로 바뀐다
// staff가 뒤로 가면?
console.log(salary + bonus + "만원" + staff);
// 상황에 따라서 값이 달라짐

console.log(staff + String(salary + bonus) + "만원");
