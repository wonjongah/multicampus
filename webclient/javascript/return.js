// 리턴값이 없을 경우 파이썬은 None, 자스는 undefined

// 내부 함수, 함수 내부에 있는 함수
// 함수 충돌을 막기 위해

function outer() {
    var outvalue = 5678;
    function inner() {
    var invalue = 1234;
    console.log("outvalue = " + outvalue);
    }
    // 안에서 밖의 것을 쓸 때 -> closer
    inner();
    console.log("invalue = " + invalue);// 에러
    }
    outer();