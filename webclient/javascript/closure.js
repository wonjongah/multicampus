function outcount(interval){
    var count = 0;
    // setInterval은 몇 초마다 호출해달라
    var id = setInterval(function(){
        count++;
        if(count == 20){
            clearInterval(id);
        }
        console.log(count + "초 지났습니다");
    }, interval); // interval은 클로저 아님, 내부에서 사용하지 않으니까
}  // id, interval 다 클로저, 내부에서 또 씀
outcount(500);
// 클로저 변수 생김, 즉 각자 변수가 힙에 있단 말
// 0.5초로 설정
outcount(1000);
// 클로저 변수 생김
// 1초로 설정

// function outcount(interval){
//     var count = 0;
  
//     var id = setInterval(()=>{
//         count++;
//         if(count == 20){
//             clearInterval(id);
//         }
//         console.log(count + "초 지났습니다");
//     }, interval); 
// }

// outcount(500);