SELECT num,
CONCAT(CAST(price AS CHAR(10)), 'X', CAST(amount AS CHAR(4)), '=') AS '단가 X 수량',
price * amount AS '구매액'
FROM buytbl;


SELECT '100' + '200';  -- 정수로 변환해서 계산을 해버림
SELECT CONCAT('100', '200');  -- 문자열 잇기
SELECT CONCAT(100,'200');  -- 콘캣이 원하는 건 문자열이기 때문에 정수를 문자열로 바꿈
SELECT 1 > '2mega';  -- 앞에 숫자 있으면 뒤의 문자열 버리고 숫자로 변환
SELECT 3 > '2mega';
SELECT 0 = 'mega2';  -- 문자는 0으로 변환