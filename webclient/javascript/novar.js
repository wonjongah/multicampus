// var score = 100;
// 전역변수 없는데?? 밑의 스코어는 뭐냐?
// 전역으로 된다...전역변수로..찍힘
// 변수를 검색하는 순서를 생각! 
// 지역변수를 스캔, 그다음 상위스코프(전역), 더 올라갈 데 없으면 거기서 변수를 만듦
// 전역에 없으면 거기에 변수를 만든다는 것..
// 가독성이 좋지 않음, 전역, 지역 불분명
// 추천사항은 선언하고 쓰기


function func(){
    var score = 100;
    scre = 77;
    console.log("함수 안 score = " + score);
    // var이 없으면? 그럼 바깥으로..
    // 파이썬에선 global이라고 써야 하는데 자바스크립트는 안 써도 된다..
    // 현재 없기 때문에 전역을 본다
}

func();

console.log("함수 밖 score = " + scre)