var ar = [[0, 1, 2, 3], [4, 5, 6], [7, 8]];
for (var i = 0; i < ar.length; i++) {
    // ar.length제일 바깥에 있는 배열의 엘리먼트 값 -> 3
    for (var j = 0; j < ar[i].length; j++) {
    // ar[i].length 각각의 길이
        console.log("ar[" + i + "][" + j +"] =" + ar[i][j]);
    }
    console.log();
}

