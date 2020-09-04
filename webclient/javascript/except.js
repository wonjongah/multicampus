function func(){
    if(true)
    throw "예외가 발생했습니다"; // 강제로 예외 발생
}

try{
    func();
}
catch(exception){
    console.log(exception);
}
console.log("실행을 완료했습니다");