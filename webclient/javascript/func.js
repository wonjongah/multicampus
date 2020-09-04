// 매개변수의 수가 맞지 않아도 에러가 아님...
// 즉 지정하지 않은 곳에는 undefined으로, 선언은 했는데 값은 없는 경우
// 인수가 더 많은 경우 넘치는 인수 무시

function sum(n) {
    if (n == undefined)
    // 값이 없을 경우, 지정값을 주고 싶다
    n = 100;
    // n = n || 100;
    // 결정된 그 순간의 값이 리턴된다, T F가 리턴되는 게 아니라, 마지막 연산의 트루를
    // 결정지을 값이 뭐냐? 위는  F || T이니까 100이 넘어감
    var s = 0;
    for (var i = 0; i <= n; i++) {
    s += i;
    }
    return s;
    }
    console.log("1~10 = " + sum(10));
    console.log("1~100 = " + sum());



    // 생략했을 때 주어지는 디폴트값
    // es6표준에 들여온
    function sum(n=100) {
        var s = 0;
        for (var i = 0; i <= n; i++) {
        s += i;
        }
        return s;
        }
        console.log("1~10 = " + sum(10));
        console.log("1~100 = " + sum());