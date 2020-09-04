//  typeof [ ]  object -> 배열도 객체다!
// 키 파트에 따옴표 붙여도 되고 안 붙여도 된다(파이썬과의 차이점)

var human = {
    name: "김상형",
    age: 29
};

var dog = {
    type: "치와와",
    weight: 2,
    male: true
}

console.log("name = " + human.name);
console.log("age = " + human.age);

// 사전이 아니라 객체다!!
// 없는 키에 대해서는 undefined
console.log("종류 = " + dog.type);
console.log("몸무게 = " + dog.weight);

// human.name or human['name'] 둘 다 가능
// 내가 접근하고자 하는 녀석을 변수로 가지고 있을 때 변수로 쓸 수 있음