var score = 100;

function func(){
    var score = 77;
    console.log("함수 안 score = " + score);
    // 지역변수 우선순위로 가서 지역변수로 간다
}

func();

console.log("함수 밖 score = " + score)
