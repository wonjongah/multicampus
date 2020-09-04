USE sqldb;

SELECT * FROM usertbl;

SELECT * FROM buytbl;

SELECT * FROM usertbl WHERE NAME = '김경';

SELECT userID, NAME
FROM usertbl
WHERE birthYear >= 1970 AND height >= 182;

SELECT userID, NAME
FROM usertbl
WHERE birthYear >= 1970 or height >= 182;

SELECT userID, NAME 
FROM usertbl
WHERE height BETWEEN 180 AND 183;  -- and 연산이랑 같은 결과

SELECT NAME, addr
FROM usertbl
WHERE addr IN('경남', '전남', '경북');  -- arrd = '경남' or addr = '전남' or addr = '경북'

SELECT NAME, height
FROM usertbl
WHERE NAME LIKE '김%';

SELECT NAME, height
FROM usertbl
WHERE NAME LIKE '_종신';