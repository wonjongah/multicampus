var menu = 1;
switch(Number(menu)){
    case 1:
        console.log("전화를 겁니다");
        //break;
        // 브레이크 안 하면 브레이크를 만날 때까지 쭉 감
    case 2:
        console.log("문자를 보냅니다");
        break; 
    case 3:
        console.log("영상통활를 연결합니다");
        break;
    default:
        console.log("잘못 입력하셨습니다");
        break;
}


var day = "월";

switch(day){
    case "월":
        console.log("일주일의 시작입니다");
        break;
    case "화":
    case "수":
    case "목":
        console.log("화수목중 하나");
        break;
    case "금":
        console.log("금");
        break;
    case "토":
    case "일":
        console.log("토일");
        break;
}