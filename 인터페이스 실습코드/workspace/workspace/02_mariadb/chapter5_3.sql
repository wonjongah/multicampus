SELECT if(100>200, '참이다', '거짓이다');

SELECT IFNULL(NULL, '널이군요'), IFNULL(100,'널이군요');

SELECT NULLIF(100,100), NULLIF(200,100);

SELECT ASCII('a'), CHAR(65);

SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc');   -- char_length는 글자수!, length는 바이트수
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');

SELECT CONCAT_WS('/', '2022', '01', '01'); -- 파이썬의 조인과 비슷
