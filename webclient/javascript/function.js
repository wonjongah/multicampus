var fn = function(){
    console.log("Hello javascript");
}
console.log(fn);

fn();

// 함수를 변수에 대입할 수 있음, 일급시민, 매개변수로 전달 가능하고 리턴값으로 함수 사용 가능

var add = function(a, b){
    return a+b;
}

var multi = function(a, b){
    return a * b;
}

function calc(a, b, f){
    return f(a, b);
}

console.log("2 + 3 = " + calc(2, 3, add));
console.log("2 * 3 = " + calc(2, 3, multi));

console.log("2 + 3 = " + calc(2, 3, (a, b)=>a+b));
console.log("2 + 3 = " + calc(2, 3, (a,b)=>a*b));
// 람다함수와 비슷한 개념의 => 함수

function outer(){
    return function(){
        console.log("hello function");
    }
}

outer()();

var fn = outer();
fn();

// 클로저~

function test(name){
    var output = "Hello" + name;

    return function(){
        console.log(output)
    }
}

var test_1 = test("Node");
var test_2 = test("Javascript");

test_1();
test_2();


// var test_1 = test("Node");을 실행시
// 힙 영역에 스코프로 노드 이름을 가진 지역변수 name과 Hello node란 output 생성
// test 끝났을 때 가리키는 것 사라짐.. 그러나 test_1이 가리키고 있기 때문에
// 가비지가 안 된다 아직 가리키고 있는 것 있음

// 클로저가 생성될 때는 var test_1 = test("Node"); 외부함수가 호출될 때
// 그것을 사용하는 시점은test_1();
// test_2(); 내부함수가 호출됐을 때
