// 암묵적 변환
// 다른 데이터 타입을 어떻게 해석할 거냐
// + 연산자일 경우 문자열이 우선순위가 높음
// 문자열 + 다른 타입일 경우 다른 타입이 문자열로 자동변환
// 나머지 연산자 - * 모듈연산 등은 숫자가 우선!
// 숫자 이외의 타입이 숫자로 자동변환

var name = "김상형 : ";
var score = 98;
console.log(name + score);
// 플러스니까 문자열로 이어지겠다

var value1 = "8";
var value2 = "6";
var add = value1 + value2;
// 플러스, 문자열로
console.log("add : " + add);

var sub = value1 - value2;
// 마이너스, 숫자로
console.log("substract : " + sub);
console.log(name - score); // NaN이 나온다 문자열을 숫자로 바꾸려는데 바꿀 수가 없으니
// NaN이 나온다

// 더하기냐 아니냐!! 암시적 변환에서 생각해야 함