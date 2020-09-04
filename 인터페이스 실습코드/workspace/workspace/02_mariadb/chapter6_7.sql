USE sqlDB;
SELECT stdName, addr FROM stdTBL
UNION ALL
SELECT clubName, roomNo FROM clubtbl;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' 
FROM userTBL
WHERE name NOT IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;


SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' 
FROM userTBL
WHERE name IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;