var human = {
    name: "김상형",
    age: 29,
    intro: function() {
    console.log("name = " + this.name);
    console.log("age = " + this.age);
    },
    toString: function(){
        return "Human " + this.name
    }
    };
   // human.intro();
    // 출력하고 싶을 때 내부에 아예 함수를 써서 호출하면 출력

    console.log(human.toString());
    // { name: '김상형', age: 29, intro: [Function: intro] } 이렇게 출력
    // toString()이라는 함수가 호출된다