// ○ null
//  아무것도 참조하지 않음을 나타냄
// ○ undefined
//  초기화 되지않은 변수가 가지는 값
// ○ NaN (not a number)
//  연산결과가 숫자가 아님
// 숫자를 기대했는데 숫자 아닐 경우
// ○ infinite
//  무한대 숫자
// 0으로 나눌 때

var notinit;

console.log("초기화되지 않은 변수 : " + notinit);
// console.log("존재하지 않은 변수 : " + ghost);

var veryBig = 1234/0;
console.log("veryBig = " + veryBig);

var noNumber = Math.sqrt(-2);
console.log("noNumber = " + noNumber);

