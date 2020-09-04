// 누가 호출했느냐에 따라서 자동으로 생성된다
var person = {
    name: "홍길동",
    eat: function(food){
    } //this.name이 아니고 name만 쓴다면? 먼저 지역변수 체크
} // 하지만 지역변수에 없음, 다음 전역변수 체크, 없음 죽음

person.eat("피자");

var human = {
    name: "김상형",
    age: 29,
    address: {
        city: "하남시",
        dong: "덕풍동",
        bunji: 673
    }
    // 객체 안에 객체 생성!! ..
}

console.log("휴먼의 주소의 시티 = " + human.address.city);