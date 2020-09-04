// def fn(*args) -> 파이썬의 가변인수, 튜플


function sumAll() {
    var sum = 0;
    for(var i=0; i<arguments.length; i++) {
        // arguments에 전달된 매개변수가 담겨있음, 배열이라고 생각하면 된다
        // arguments는 자바스크립트에서 제공되는, 함수 안의 키워드다
        // 인수들의 값들이 여기에 담겨있다
    sum += arguments[i];
    }
    return sum;
    }
console.log(sumAll(1,2,3,4,5,6,7,8,9))



function sumAll() {
    var sum = 0;
    for(let i of arguments) {
        // arguments에 전달된 매개변수가 담겨있음, 배열이라고 생각하면 된다
        // arguments는 자바스크립트에서 제공되는, 함수 안의 키워드다
        // 인수들의 값들이 여기에 담겨있다
    sum += i;
    }
    return sum;
    }
console.log(sumAll(1,2,3,4,5,6,7,8,9))
