// ○ 다른 언어에서는 동일한 데이터 타입에 대해서 배열 생성 가능
// ○ 자바스크립트는 어떠한 종류의 자료형도 배열 요소가 될 수 있음
//     자바스크립트의 모든 자료형을 넣을 수 있음
// 파이썬의 리스트와 유사
// {} -> 파이썬에선 사전, 자바스크립트에선 객체
// 둘은 비슷~ 

for (var i = 0; i < 5; i++){
    console.log("좋은 아침입니다")
}

var arScore = [88,78,96,54,23];

for(var st = 0; st<5; st++){
    console.log((st+1) + "번째 학생의 성적 : " + arScore[st]);
}

var sum = 0;
for(var st = 0; st < arScore.length; st++){
    sum += arScore[st];
}

console.log("총점 : " + sum + ", 평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`)


var sum = 0;
for(var i = 1; i <= 100; i++){
    sum += i;
}
// for i in range(100)
console.log("1~100까지의 합 = " + sum)


// for in이라는 반복문!!
// for(let i in array)
// 루프가 돌 때마다 0부터 인덱스를 i에 넣어준다

sum = 0;

for(let ix in arScore){
    sum += arScore[ix];
}

console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`)
sum = 0;

// for of라는 반복문, 굳이 인덱스 없고 계속 돌 거라면

for(let score of arScore){
    sum += score;
    // 인덱스가 아니라 값을 score에 넣어서 리턴해준다
}
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`)
