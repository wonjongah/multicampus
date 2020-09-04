// 동적으로 속성 추가

var student = {};

student.name = "홍길동";
student.hobby = "악기";
student.special = "프로그래밍";
student.department = "생명공학과";

student.toString = function(){
    for(var key in this){
        if(key != 'toString'){  // 자신이면 출력 안 함
            console.log(key + '\t' + this[key]);
        }
    }
}
console.log(student);

for(let key in student){  //student가 배열이면 key에는 인덱스가!, 베열이 아니고 객체면
    // 속성명이 키에 전달된다
    console.log(key, student[key]);
    // 변수명으로 전달할 때는 []대괄호로!
    // 속성명과 속성값을 순회하면서 출력하는 코드
}

delete student.hobby;
student.toString();
console.log("name" in student);
console.log("성별" in student);

// cross browsing 문제, 다른 브라우저를 사용해도 사용 가능하지 않은.. 문제
// 선택을 해야 한다

// new 키워드로 객체 생성 힙에 인스턴스 만들겠다
// this는 새로 생긴 인스턴스를 가리킴
